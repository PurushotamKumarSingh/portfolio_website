from django.core import validators 
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','subject','messages']
        labels = {'name':'Enter Your Name', 'email':'Enter Your Email','subjects':'Your Subject','messages':'Your Message'}
        error_messages = {'email':{'required':'Must Enter your Emailid'},
                          'messages':{'required':'Write few words'}}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'messages':forms.TextInput(attrs={'class':'form-control'})
        }
