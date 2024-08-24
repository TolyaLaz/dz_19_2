import secrets
import random
from string import ascii_letters, digits
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.views.generic import  CreateView, FormView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.hashers import make_password
from users.forms import UserRegisterForm, ResetPasswordForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}/'
        send_mail(
            subject='Подтверждение регистрации',
            message=f'Для подтверждения регистрации перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_varification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return  redirect(reverse('users:login'))

class ResetPasswordView(FormView):
    template_name = 'users/reset-password.html'
    form_class = ResetPasswordForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        new_password = "".join(random.sample(digits + ascii_letters, 8))
        user = get_user_model().objects.get(email=email)
        user.password = make_password(new_password)
        user.save()
        send_mail(
            'Восстановление пароля',
            f'Ваш пароль был сброшен. Ваш новый пароль {new_password}',
            None,
            recipient_list=[email],
        )
        return super().form_valid(form)