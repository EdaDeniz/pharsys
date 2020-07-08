from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from carts.models import Cart
from .forms import CustomUserCreationForm


class SignUpView(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        obj = form.save()
        Cart.objects.create(user=obj)
        return redirect('home')
