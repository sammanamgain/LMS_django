from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.utils import timezone
from django.views.decorators.http import require_http_methods
# Create your views here.
def Home(request):
    data={'Name':'Samman'}
    return render(request,'Home.html', context={'data':data})



@csrf_exempt
def createUser(request):
   
    if request.method != 'POST':
        return
    try:
        data=json.loads(request.body.decode('utf-8'))
        Name=data['Name']
        Email=data['Email']
        membership_date=timezone.now().date()
        user=User(Name=Name,Email=Email,membership_date=membership_date)
        user.save()
        print(Name,Email,membership_date)
        return JsonResponse({'success':True})
    except json.JSONDecodeError:
        return JsonResponse({'error':'Invalid data'},status=400)

    except Exception as e:
        return JsonResponse({'error':str(e),'message':'sorry failed on add on database'},status=400)
    
        
    