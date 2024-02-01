from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User,Book
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
# Create your views here.
def Home(request):
    data={'Name':'Samman'}
    return render(request,'Home.html', context={'data':data})


#create a user
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
    
        
 #get all user   
def getAllUser(request):
    try:
        if request.method != 'GET':
            return JsonResponse({"status":"invalid request type"})
        users=User.objects.all()
        user_data = [{'id': user.user_id, 'username': user.Name, 'email': user.Email} for user in users]
      
        return JsonResponse({'fetch':True,'data':user_data})
    except Exception as e:
        return JsonResponse({'exception':e})
    

#get a single user
    
def getUser(request,user_id):
    try:
        if request.method != 'GET':
            return JsonResponse({'message':'Bad Request'},status=400)
        user= get_object_or_404(User, pk=user_id)
        user_data={
            'Name':user.Name,
            'Email':user.Email,
            'Membership_Date':user.membership_date
        }
        return JsonResponse({'success':True,'user':user_data})

    except Exception as e:
        return JsonResponse({'exception':e})
   
@csrf_exempt 
def addBook(request):
    try:
      if request.method!='POST':
          return JsonResponse({'message':'Invalid call'},status=404)
      data=json.loads(request.body.decode('utf-8'))
      cleaned_data={'title':data['title'],'isbn':data['isbn'],'published_date':data['published_date'],'genre':data['genre']}
      book=Book(**cleaned_data)
      book.save()
      return JsonResponse({'Success':True,'message':'successfully created '})
    except Exception as e:
        return JsonResponse({'message':e},status=400)