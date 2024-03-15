from django.shortcuts import render

# Create your views here.
def training(request):
    context = {'training':'active'}
    return render(request,'training/training.html',context)
