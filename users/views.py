import random

from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
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
        new_user = form.save()
        verification = ''.join([str(random.randint(0, 9)) for i in range(12)])
        new_user.email_verification = verification
        send_mail(
            subject='Потверждение почты',
            message=f'Подтвердите вашу почту. Перейдите по ссылке: http://127.0.0.1:8000/users/activate/{verification}',
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
    for use in User.objects.all():
        if use.email_verification == uid:
            use.email_is_active = True
            use.save()
            return redirect(reverse('users:email_activated'))
    return redirect(reverse('users:email_activated'))


def restore_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        for use in User.objects.all():
            if use.email == email:
                new_password = ''.join([str(random.randint(0, 9)) for i in range(12)])
                send_mail(
                    subject='Восстановление пароля',
                    message=f'Ваш новый пароль: {new_password}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[use.email]
                )
                use.set_password(new_password)
                use.save()
    return render(request, "users/restore_password.html")
