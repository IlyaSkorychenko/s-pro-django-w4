from django.urls import path
from .views import BookListView, BookCreationFormView, ReviewViewForm, BookView

urlpatterns = [
    path('', BookListView.as_view(), name='all-books'),
    path('<int:pk>', BookView.as_view()),
    path('create', BookCreationFormView.as_view()),
    path('<int:id>/review', ReviewViewForm.as_view()),
]
