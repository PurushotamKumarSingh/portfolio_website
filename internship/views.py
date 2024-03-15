from django.shortcuts import render

# Create your views here.
def internship(request):
    context = {'internship':'active'}
    return render(request,'internship/internship.html',context)
