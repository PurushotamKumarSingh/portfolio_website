from django.urls import path
from . import views

urlpatterns = [
    path('qualifications/',views.qualifications,name='qualifications')
]
