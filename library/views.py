from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Book, BorrowedBooks
from .serializers import (
    UserSerializer,
    BookSerializer,
    BookDetailsSerializer,
    BorrowedBooksSerializer,
)


# Api for user
class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListUsersView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class GetUserView(APIView):
    def get(self, request, id, *args, **kwargs):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


# Api for books
class AddBookView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBooksView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class GetBookView(APIView):
    def get(self, request, id, *args, **kwargs):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class BookDetailsView(APIView):
    # This method to assign details to a book or update existing book details,
    def post(self, request, *args, **kwargs):
        serializer = BookDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Api for borrowing


class BorrowBookView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BorrowedBooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnBookView(APIView):
    def put(self, request, id, *args, **kwargs):
        return self.update_book(request, id)

    def patch(self, request, id, *args, **kwargs):
        return self.update_book(request, id)

    def update_book(self, request, id):
        borrowed_book = BorrowedBooks.objects.get(id=id)
        serializer = BorrowedBooksSerializer(
            borrowed_book, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBorrowedBooksView(APIView):
    def get(self, request, *args, **kwargs):
        borrowed_books = BorrowedBooks.objects.all()
        serializer = BorrowedBooksSerializer(borrowed_books, many=True)
        return Response(serializer.data)
