from .forms import LoginForm
from django.contrib.auth import login
from django.contrib.auth.models import *
from .serializers import *
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated

class HomeView(LoginRequiredMixin, TemplateView):#「LoginRequiredMixin → TemplateView」この順番で記述しないとログイン必須機能が表れないので注意！！
    template_name = 'home.html'
    login_url = '/login/'
    model = CustomUser
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
      ctx = {
          'username': self.request.user.username
      }
      return self.render_to_response(ctx)

class MyLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

class MyLogoutView(LogoutView):
    template_name = 'logout.html'
    

    
    