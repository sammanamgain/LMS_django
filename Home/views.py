from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User as USER
from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User, Book, BookDetails, BorrowedBooks
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from datetime import timedelta
from django.core.serializers import serialize
# Create your views here.


def Home(request):
    data = {'Name': 'Samman'}
    return render(request, 'Home.html', context={'data': data})


# create a user
@login_required
@csrf_exempt
def createUser(request):

    if request.method != 'POST':
        return
    try:
        data = json.loads(request.body.decode('utf-8'))
        Name = data['Name']
        Email = data['Email']
        membership_date = timezone.now().date()
        user = User(Name=Name, Email=Email, membership_date=membership_date)
        user.save()
        print(Name, Email, membership_date)
        return JsonResponse({'success': True})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid data'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e), 'message': 'sorry failed on add on database'}, status=400)

 # get all user


@login_required
def getAllUser(request):
    try:
        if request.method != 'GET':
            return JsonResponse({"status": "invalid request type"})
        users = User.objects.all()
        user_data = [{'id': user.user_id, 'username': user.Name,
                      'email': user.Email} for user in users]

        return JsonResponse({'fetch': True, 'data': user_data})
    except Exception as e:
        return JsonResponse({'exception': e})


# get a single user
@login_required
def getUser(request, user_id):
    try:
        if request.method != 'GET':
            return JsonResponse({'message': 'Bad Request'}, status=400)
        user = get_object_or_404(User, pk=user_id)
        user_data = {
            'Name': user.Name,
            'Email': user.Email,
            'Membership_Date': user.membership_date
        }
        return JsonResponse({'success': True, 'user': user_data})

    except Exception as e:
        return JsonResponse({'exception': e})


@login_required
@csrf_exempt
def addBook(request):
    try:
        if request.method != 'POST':
            return JsonResponse({'message': 'Invalid call'}, status=404)
        data = json.loads(request.body.decode('utf-8'))
        cleaned_data = {'title': data['title'], 'isbn': data['isbn'],
                        'published_date': data['published_date'], 'genre': data['genre']}
        book = Book(**cleaned_data)
        book.save()
        return JsonResponse({'Success': True, 'message': 'successfully created '})
    except Exception as e:
        return JsonResponse({'message': e}, status=400)


@login_required
def getAllBook(request):
    try:
        if request.method != 'GET':
            return JsonResponse({'message': 'Invalid call'}, status=400)
        data = Book.objects.all()

        alldata = [{'title': book.title, 'isbn': book.isbn,
                    'published_date': book.published_date, 'genre': book.genre} for book in data]

        return JsonResponse({'Message': alldata})

    except Exception as e:
        return JsonResponse({'message': e}, status=400)

# fetch all book details


@login_required
def getBookdetails(request, book_id):
    try:
        if request.method != 'GET':
            return JsonResponse({'message': 'Invalid call'}, status=400)

        book = get_object_or_404(Book, pk=book_id)
        Book_Details = get_object_or_404(BookDetails, book=book_id)
        books = {'title': book.title, 'isbn': book.isbn,
                 'published_date': book.published_date, 'genre': book.genre, 'details_id': Book_Details.details_id,  'number_of_pages': Book_Details.number_of_pages, 'publisher': Book_Details.publisher, 'language': Book_Details.language}

        return JsonResponse({'Message': books, })
    except Http404:
        return JsonResponse({'message': 'Book not found'}, status=404)

    except Exception as e:
        return JsonResponse({'message': e}, status=400)


@login_required
@csrf_exempt
def AddBookDetails(request):
    try:
        if request.method != 'POST':
            return JsonResponse({'message': 'Invalid call'}, status=400)

        data = json.loads(request.body.decode('utf-8'))
        book_id = data.get('book_id')
        if not book_id:
            return JsonResponse({'message': 'Book ID is required'}, status=400)

        book = get_object_or_404(Book, pk=book_id)

        cleaned_data = {'details_id': data['details_id'], 'book': book,
                        'number_of_pages': data['number_of_pages'], 'publisher': data['publisher'], 'language': data['language']}
        book = BookDetails(**cleaned_data)
        book.save()

        return JsonResponse({'Message': 'Successfully added'})
    except Http404:
        return JsonResponse({'message': 'Book not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)


@login_required
@csrf_exempt
def BorrowBook(request):
    try:
        if request.method != 'POST':
            return JsonResponse({'message': 'Invalid call'}, status=400)

        data = json.loads(request.body.decode('utf-8'))
        book_id = data.get('book_id')
        user_id = data.get('user_id')

        if not book_id:
            return JsonResponse({'message': 'Book ID is required'}, status=400)

        book = get_object_or_404(Book, pk=book_id)
        user = get_object_or_404(User, pk=user_id)
        borrowed_date = timezone.now().date()
        returned_date = borrowed_date+timedelta(days=30)

        cleaned_data = {'book': book, 'user': user,
                        'borrow_date': borrowed_date, 'return_date': returned_date}
        book = BorrowedBooks(**cleaned_data)
        book.save()

        return JsonResponse({'Message': 'Successfully added'})
    except Http404:
        return JsonResponse({'message': 'Book not found or User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)


@login_required
def getAllBorrow(request):
    try:
        if request.method != 'GET':
            return JsonResponse({'message': 'Invalid call'}, status=400)

        data = BorrowedBooks.objects.all()

        # Serialize the queryset to JSON
        serialized_data = serialize('json', data)

        # Convert the serialized data to Python objects
        parsed_data = json.loads(serialized_data)

        # Extract relevant fields from the parsed data
        alldata = [
            {
                'borrowed_books_id': borrow['pk'],
                'user': borrow['fields']['user'],
                'book': borrow['fields']['book'],
                'borrow_date': borrow['fields']['borrow_date'],
                'return_date': borrow['fields']['return_date'],
            }
            for borrow in parsed_data
        ]

        return JsonResponse({'Message': alldata})

    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)


@login_required
@csrf_exempt
def deleteBorrowBook(request):
    try:
        if request.method != 'DELETE':
            return JsonResponse({'message': 'Invalid call'}, status=400)

        data = json.loads(request.body.decode('utf-8'))
        book_id = data.get('book_id')
        user_id = data.get('user_id')

        borrowed_book = get_object_or_404(
            BorrowedBooks, user=user_id, book=book_id)

        # Delete the record
        borrowed_book.delete()

        return JsonResponse({'Message': 'Successfully Deleted'})
    except Http404:
        return JsonResponse({'message': 'Book not found or User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)


@login_required
@csrf_exempt
def signup(request):
    print('signup')
    try:
        if (request.method != 'POST'):
            return JsonResponse({'message': 'Invalid call'})
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        user = USER.objects.create_user(username=username, password=password)
        login(request, user)
        return JsonResponse({'success': True, 'message': 'User created successfully'})
    except Exception as e:
        return JsonResponse({'message': 'failed', 'error': str(e)})


@csrf_exempt
@login_required
def Login(request):

    try:
        if (request.method != 'POST'):
            return JsonResponse({'message': 'Invalid call'})
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        user = get_object_or_404(USER, username=username)
        if not user.check_password(password):
            return JsonResponse({'message': 'Invalid User||wrong  Password'})
        if user is None:
            return JsonResponse({'message': 'Invalid User||wrong  username and password'})
        login(request, user)
        return JsonResponse({'success': True, 'message': 'User Looged In successfully'})
    except Exception as e:
        return JsonResponse({'message': 'failed', 'error': str(e)})
