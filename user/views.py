from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class RegisterView(CreateView):
    """
    Registers a user to the application.
    """
    template_name = 'user/register.html'
    form_class = UserCreationForm
