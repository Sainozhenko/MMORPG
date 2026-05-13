import pandas as pd
from django.core.management.base import BaseCommand
from website.models import L2Server  # Должно соответствовать имени твоего приложения

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_path = 'l2_fake_database.xlsx'
        df = pd.read_excel(file_path, sheet_name='Servers')
        for _, row in df.iterrows():
            L2Server.objects.update_or_create(
                name=row['name'],
                defaults={
                    'server_type': row['type'],
                    'opening_date': str(row['date']) if pd.notna(row['date']) else "",
                    'online_count': row['online'],
                    'status': row['status']
                }
            )
        self.stdout.write(self.style.SUCCESS('Data loaded!'))