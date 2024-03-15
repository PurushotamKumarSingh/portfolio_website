from django.shortcuts import render

# Create your views here.
def qualifications(request):
    context = {'qualifications':'active'}
    return render(request,'qualifications/qualifications.html',context)