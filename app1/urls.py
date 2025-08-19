from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_form, name='home'),  # homepage
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('feedback/list/', views.feedback_list, name='feedback_list'),
]
