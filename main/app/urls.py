from django.urls import path
from . import views


urlpatterns = [
    path('books', views.BookListView.as_view()),
    path('books/new', views.NewBookView.as_view()),
]