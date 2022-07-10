from django.urls import reverse_lazy
from django.views.generic import FormView
from bookstore.forms import BookForm, SearchBookForm, ReviewForm
from .base_views import FormViewWithAuth, TemplateViewWithAuthStatus, DetailViewWithAuthStatus
from .models import Book


class BookListView(TemplateViewWithAuthStatus):
    template_name = 'bookstore/books_lis.html'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        search_form = SearchBookForm(self.request.GET)
        books = Book.objects.all()

        if search_form.is_valid():
            books = Book.objects.filter(title=self.request.GET['title'])
        context['books'] = books
        context['search_book_form'] = SearchBookForm

        return context


class BookView(DetailViewWithAuthStatus):
    model = Book
    template_name = 'bookstore/book.html'


class BookCreationFormView(FormView):
    form_class = BookForm
    success_url = reverse_lazy('all-books')
    template_name = 'bookstore/book_form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ReviewViewForm(FormViewWithAuth):
    form_class = ReviewForm
    success_url = reverse_lazy('all-books')
    template_name = 'bookstore/review_form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        user = self.request.user
        book = Book.objects.get(pk=self.kwargs['id'])
        fom = form_class(user, book, **self.get_form_kwargs())

        return fom

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
