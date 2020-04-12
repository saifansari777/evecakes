from django.urls import path
from .views import Userlogin
app_name = 'user'

urlpatterns = [path('login/', Userlogin.as_view(), name='user-login')]