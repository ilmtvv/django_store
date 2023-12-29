from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserForm, ProfileForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:succes')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='поздравляем с регистрацией',
            message=f'http://127.0.0.1:8000/users/register/{new_user.uuid}/',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('user:uupdate')
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    print(request)
    new_pass = User.objects.make_random_password()
    send_mail(
        subject='новый пароль',
        message=f'{new_pass}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_pass)
    request.user.save()
    return redirect(reverse('users:login'))


def succes(request):
    return render(request, 'users/succes.html')


def confirm(request, uuid):
    user = get_object_or_404(User, uuid=uuid)
    user.is_active = True
    user.save()
    return render(request, 'users/confirm.html', {'uuid': uuid})