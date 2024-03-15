from django.urls import path
from . import views

urlpatterns=[
    path('internship/',views.internship,name='internship'),
]