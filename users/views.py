from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import ListView

from users.forms import CustomUserCreationForm
from users.models import CustomUser
from users.models import Pending


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


class UserListView(ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        ids = Pending.objects.filter(
            sender__pk=self.request.user.pk,
        ).values_list(
            f'{Pending.recipient.field.name}__{CustomUser.id.field.name}',
        )
        return CustomUser.objects.exclude(pk__in=ids)

    def post(self, request, *args, **kwargs):
        recipient_pk = int(request.POST.getlist('recipient')[0])

        if self.request.user.pk != recipient_pk:
            Pending.objects.get_or_create(
                sender=CustomUser.objects.filter(pk=self.request.user.pk)[0],
                recipient=CustomUser.objects.filter(pk=recipient_pk)[0],
            )

        return redirect('users:user_list')


class PendingListView(ListView):
    model = Pending
    template_name = 'users/pending_list.html'
    context_object_name = 'pendings'

    def get_queryset(self):
        return Pending.objects.filter(
            sender__pk=self.request.user.pk,
        ) | Pending.objects.filter(
            recipient__pk=self.request.user.pk,
        )
