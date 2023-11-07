import random

from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        verification = gen_verification_code_or_password()
        new_user.email_verification = verification
        new_user.is_active = False
        verification_url = f'http://127.0.0.1:8000/users/activate/{verification}'
        send_mail(
            subject='Потверждение почты',
            message=f'Подтвердите вашу почту. Перейдите по ссылке: {verification_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        new_user.save()

        return super().form_valid(form)


class ProfilerView(UpdateView):
    model = User
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def email_activated(request):
    return render(request, "users/email_activated.html")


def activate(request, uid):
    user = get_object_or_404(User, email_verification=uid)
    user.is_active = True
    user.save()
    return redirect(reverse('users:email_activated'))


def restore_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        new_password = gen_verification_code_or_password()
        send_mail(
            subject='Восстановление пароля',
            message=f'Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse('users:login'))
    return render(request, "users/restore_password.html")


def gen_verification_code_or_password():
    return ''.join([str(random.randint(0, 9)) for i in range(12)])
