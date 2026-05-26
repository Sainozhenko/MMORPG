from django import forms
from allauth.account.forms import LoginForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomLoginForm(LoginForm):
    def clean(self):
        # 1. Сначала берем данные, которые ввел пользователь
        login = self.cleaned_data.get("login")
        password = self.cleaned_data.get("password")
        
        # 2. Если логин и пароль есть, проводим твою проверку
        if login and password:
            user = User.objects.filter(username=login).first() or \
                   User.objects.filter(email=login).first()
            
            # Разделение ошибок:
            if not user:
                raise forms.ValidationError("Account does not exist.")
            
            # Проверяем пароль только если пользователь найден
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password.")
        
        # 3. ВАЖНО: вызываем super().clean(), чтобы Allauth доделал свою работу
        # (он проверит email, сессии и т.д.)
        return super().clean()