from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import UserFollows
from .forms import UserFollowsForm


class UserFollowsView(CreateView):
    model = UserFollows
    form_class = UserFollowsForm
    success_url = reverse_lazy('users:follows')
    template_name = 'users/follows.html'

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
