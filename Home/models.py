from django.db import models

# Create your models here.
#user model 
class User(models.Model):
    
    user_id = models.AutoField(primary_key=True)  
    Name = models.CharField(max_length=255)
    Email = models.EmailField(default='default@gmail.com')
    membership_date = models.DateField()

#creating the Book model to store information of the each book
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)
    
#creating the Bookdetails model

class BookDetails(models.Model):
    details_id = models.AutoField(primary_key=True)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, unique=True)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    
#creating a table to stored borrowed books

class BorrowedBooks(models.Model):
    borrowed_books_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()
