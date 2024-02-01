from django.test import TestCase
import pytest
from django.test import RequestFactory
from .views import getAllBook
from .models import Book
from mixer.backend.django import mixer
from django.http import JsonResponse


@pytest.mark.django_db
class TestGetAllBook(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_all_books_returns_single_book(self):
        # Arrange
        request = self.factory.get('/')
        mixer.blend(Book, title='Book One', isbn='12345',
                    published_date='2021-01-01', genre='Fiction')

        # Act
        response = getAllBook(request)

        # Assert
        assert response.status_code == 200
        assert 'Message' in response.content.decode()

    def test_get_all_books_returns_no_books(self):
        # Arrange
        request = self.factory.get('/')

        # Act
        response = getAllBook(request)

        # Assert
        assert response.status_code == 200
        assert 'Message' in response.content.decode()

    def test_get_all_books_single_book_different_genre(self):
        # Arrange
        request = self.factory.get('/')
        mixer.blend(Book, title='Book Two', isbn='67890',
                    published_date='2021-01-01', genre='Non-Fiction')

        # Act
        response = getAllBook(request)

        # Assert
        assert response.status_code == 200
        assert 'Message' in response.content.decode()

    def test_post_method_not_allowed(self):
        # Arrange
        request = self.factory.post('/')

        # Act
        response = getAllBook(request)

        # Assert
        assert response.status_code == 400
        assert 'message' in response.content.decode()

    def test_put_method_not_supported(self):
        # Arrange
        request = self.factory.put('/')

        # Act
        response = getAllBook(request)

        # Assert
        assert response.status_code == 400
        assert 'message' in response.content.decode()

    def test_delete_method_invalid(self):
        # Arrange
        request = self.factory.delete('/')

        # Act
        response = getAllBook(request)

        # Assert
        assert response.status_code == 400
        assert 'message' in response.content.decode()
