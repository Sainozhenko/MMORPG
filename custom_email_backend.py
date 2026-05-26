import re
from django.core.mail.backends.filebased import EmailBackend


class FixedFileEmailBackend(EmailBackend):
    def write_message(self, message):
        # Получаем оригинальный текст письма
        msg_bytes = message.message().as_bytes()
        content = msg_bytes.decode("utf-8", errors="ignore")

        # Исправляем quoted-printable: убираем мягкие переносы строк (=\n или =\r\n)
        # Именно эта магия склеит разорванную ссылку accounts/confirm-email=... обратно в одну строку!
        fixed_content = re.sub(r"=\r?\n", "", content)

        # Также убираем артефакты '=3D' (если вдруг все-таки проскочит кодирование знака равенства)
        fixed_content = fixed_content.replace("=3D", "=")

        # Записываем уже идеально чистое письмо в файл sent_emails
        self.stream.write(fixed_content.encode("utf-8"))
