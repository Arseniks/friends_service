from django.urls import reverse_lazy
from django.views.generic import FormView
from users.forms import CustomUserCreationForm

from users.models import CustomUser


class Register(FormView):
    template_name = 'users/signup.html'
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)

        user.is_active = True
        user.save()

        return super().form_valid(form)
