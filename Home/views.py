from django.shortcuts import render

# Create your views here.
def Home(request):
    data={'Name':'Samman'}
    return render(request,'Home.html', context={'data':data})