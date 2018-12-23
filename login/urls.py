from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    path('login_action/', views.login_action, name='login_action'),
    path('reset_pwd/', views.reset_pwd, name='reset_pwd'),
    path('reset_action/', views.to_un_reset, name='reset_action'),
    path('', views.logout, name='logout'),
]
