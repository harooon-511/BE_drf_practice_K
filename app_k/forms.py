from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
  class Meta:
        model = CustomUser
        fields = ['username', 'password']