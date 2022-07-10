from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1)])


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_at = models.DateField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)


class Review(models.Model):
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
