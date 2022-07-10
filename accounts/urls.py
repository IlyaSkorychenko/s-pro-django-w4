from django.urls import path
from .views import RegistrationFormView, LoginFormView, LogoutView

urlpatterns = [
    path('register', RegistrationFormView.as_view()),
    path('login', LoginFormView.as_view(), name='login'),
    path('logout', LogoutView.as_view()),
]
