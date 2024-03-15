from django.shortcuts import render

# Create your views here.
def certificate(request):
    context = {'certificate':'active'}
    return render(request,'certificate/certificate.html',context)
