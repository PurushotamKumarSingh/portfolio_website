from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def home(request):
    context = {'home':'active'}
    return render(request,'myresume/home.html',context)

def form(request):
    fm = StudentRegistration()
    return render(request,'myresume/contact.html',{"form":fm})

def send(request):

    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if  fm.is_valid():
            nm = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            subject = fm.cleaned_data['subject']
            messages = fm.cleaned_data['messages']

            reg = User(name=nm, email=email, subject=subject, messages=messages )
            reg.save()

            return redirect('form')
        else:
            fm = StudentRegistration()
   
    context = {'form':fm,'contact': 'active'}
    return render(request,'myresume/contact.html',context)