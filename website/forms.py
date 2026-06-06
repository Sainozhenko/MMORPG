from django import forms
from forum.models import Profile
from allauth.account.forms import LoginForm 
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomLoginForm(LoginForm):
    def clean(self):
        login = self.cleaned_data.get("login")
        password = self.cleaned_data.get("password")
        if login and password:
            user = User.objects.filter(username=login).first() or \
                   User.objects.filter(email=login).first()
            if not user:
                raise forms.ValidationError("Account does not exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password.")
        return super().clean()
    
class ProfileForm(forms.ModelForm):
    class Meta:
        from allauth.account.forms import LoginForm
        model = Profile  
        fields = ['avatar']