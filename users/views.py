import secrets

from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейти по ссылке {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def logout_view(request):
    logout(request)
    return redirect('/')


def recovery_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        token = secrets.token_hex(8)

        # user_recovery_password = User.objects.get(email=email)
        user_recovery_password = get_object_or_404(User, email=email) # так безопаснее на случай отсутствия пользователя
        user_recovery_password.password = make_password(token)
        user_recovery_password.save()
        send_mail(
                  subject="Смена пароля",
                  message=f"Автоматически сформированный пароль {token}",
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[email]
                )
    return render(request, 'users/recovery_password_form.html')


# class RecoveryUpdateView(UpdateView):
#     model = User
#     success_url = reverse_lazy('users:login')
#
#     def form_valid(self, form):
#         user = form.save()
#         token = secrets.token_hex(8)
#         user.password = make_password(token)
#         user.save()
#         send_mail(
#             subject="Смена пароля",
#             message=f"Автоматически сформированный пароль {token}",
#             from_email=EMAIL_HOST_USER,
#             recipient_list=[user.email]
#         )
#         return super().form_valid(form)

