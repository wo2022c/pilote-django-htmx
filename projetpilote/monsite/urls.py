from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'monsite'

urlpatterns = [
    path('', views.hello, name='hello'), # to delete
]