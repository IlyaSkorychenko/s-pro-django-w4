from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView, TemplateView, DetailView
from bookstore.mixins import AuthContextMixin


class TemplateViewWithAuthStatus(AuthContextMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super(TemplateViewWithAuthStatus, self).get_context_data(**kwargs)

        return self.get_auth_context(context)


class DetailViewWithAuthStatus(AuthContextMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super(DetailViewWithAuthStatus, self).get_context_data(**kwargs)

        return self.get_auth_context(context)


class FormViewWithAuth(AuthContextMixin, FormView):
    def get_context_data(self, **kwargs):
        context = super(FormViewWithAuth, self).get_context_data(**kwargs)

        return self.get_auth_context(context)

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))

        return super(FormViewWithAuth, self).post(request, *args, **kwargs)
