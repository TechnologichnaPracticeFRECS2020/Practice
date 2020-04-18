from django.urls import path, include
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='random-home'),
]
