from django.contrib.auth import views as auth_views  # Uma alternativa usando a variável auth_views
from django.urls import path

from .forms import AuthenticationFormCustomizado

app_name = 'autenticacao'

urlpatterns = [
    path('login/', auth_views.login, {'authentication_form': AuthenticationFormCustomizado}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
]