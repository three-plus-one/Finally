from django.urls import path
from . import views

app_name = 'station'
urlpatterns = (
    path('', views.index, name='ListCS'),
    path('<int:cs_add>/common/', views.show_common, name='show_common'),
    path('<int:cs_add>/free/', views.show_free, name='show_free'),
    path('<int:cs_add>/focus/', views.show_focus, name='show_focus'),
    path('reset/', views.to_reset, name='reset'),

    path('change_state/', views.change_state, name='change_state'),
)
