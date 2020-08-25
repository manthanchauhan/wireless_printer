from django.urls import path
from . import views

app_name = 'text_share'

urlpatterns = [
    path('', views.view_shared_text, name='text_share'),
    path('text', views.view_shared_text, name='text_share'),
    path('refresh_text', views.refresh_text, name='refresh_text'),
]
