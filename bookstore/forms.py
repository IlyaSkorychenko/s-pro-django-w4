from django import forms
from django.contrib.auth import get_user_model
from bookstore.models import Book, Review


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'published_at',
            'author_id'
        ]
        widgets = {
            'published_at': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class': 'form-control', 'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }


class SearchBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
        ]


class ReviewForm(forms.ModelForm):
    def __init__(self, user, book, *args, **kwargs):
        self.user = user
        self.book = book

        super(ReviewForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = [
            'text',
        ]

    def save(self, commit=True):
        review = super(ReviewForm, self).save(commit=False)
        review.book = self.book
        review.user = self.user

        if commit:
            review.save()

        return
