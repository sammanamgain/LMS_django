"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import Home
from Home.views import createUser, getAllUser, getUser, addBook, getAllBook, getBookdetails, AddBookDetails, BorrowBook, getAllBorrow, deleteBorrowBook, signup, Login

urlpatterns = [
    path('', Home),
    path('api/v1/getuser/<int:user_id>', getUser),
    path('api/v1/getalluser', getAllUser),
    path('api/v1/user', createUser),
    path('api/v1/addbook', addBook),
    path('api/v1/allbook', getAllBook),
    path('api/v1/book/<int:book_id>', getBookdetails),
    path('api/v1/addbookdetails', AddBookDetails),

    path('api/v1/borrow', BorrowBook),

    path('api/v1/removeborrow', deleteBorrowBook),
    path('api/v1/getallborrow', getAllBorrow),
    path('api/v1/signup', signup),
    path('api/v1/logIn', Login),
    path('admin/', admin.site.urls),
]
