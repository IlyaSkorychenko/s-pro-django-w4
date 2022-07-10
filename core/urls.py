from django.urls import path, include

urlpatterns = [
    path('', include('bookstore.urls')),
    path('', include('accounts.urls')),
]
