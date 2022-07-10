from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm


class RegistrationFormView(FormView):
    form_class = UserCreateForm
    success_url = reverse_lazy('all-books')
    template_name = 'accounts/register_form.html'

    def form_valid(self, form):
        form.save()
        
        return super(RegistrationFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('all-books')
    template_name = 'accounts/login_form.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect(reverse('all-books'))
