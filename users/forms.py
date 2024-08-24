from catalog.forms import StyleFormMixin
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, Form, ValidationError
from users.models import User
from django.contrib.auth import get_user_model


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ResetPasswordForm(StyleFormMixin, Form):
    email = EmailField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not get_user_model().objects.filter(email=email).exists():
            raise ValidationError("Такого пользователя не существует")
        return email