from django.urls import path
from .views import (
    CreateUserView,
    ListUsersView,
    GetUserView,
    AddBookView,
    ListBooksView,
    GetBookView,
    BookDetailsView,
    BorrowBookView,
    ReturnBookView,
    ListBorrowedBooksView,
)


urlpatterns = [
    # user
    path("users/create/", CreateUserView.as_view(), name="create-user"),
    path("users/list/", ListUsersView.as_view(), name="list-user"),
    path("users/<uuid:id>/", GetUserView.as_view(), name="get-user"),
    # book
    path("books/add/", AddBookView.as_view(), name="add-book"),
    path("books/list/", ListBooksView.as_view(), name="list-book"),
    path("books/<uuid:id>/", GetBookView.as_view(), name="get-book"),
    path("books/details/", BookDetailsView.as_view(), name="add-book-details"),
    # borrowedbooks
    path("borrow/", BorrowBookView.as_view(), name="borrow-book"),
    path("return/<uuid:id>/", ReturnBookView.as_view(), name="return-book"),
    path("borrowed/list/", ListBorrowedBooksView.as_view(), name="return-book"),
]
