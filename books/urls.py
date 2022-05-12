from django.urls import path
from .views import  Booksview,BooksDetailView,AddReviewBook

app_name='books'
urlpatterns = [
    path('',Booksview.as_view(),name='list'),
    path('<int:id>/',BooksDetailView.as_view(),name='detail'),
    path('<int:id>/review/',AddReviewBook.as_view(),name='review'),
]