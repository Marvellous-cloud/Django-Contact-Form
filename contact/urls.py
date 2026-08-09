from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
]