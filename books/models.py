from django.db import models
from django.utils import timezone

from users.models import CustomUser
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    book_picture = models.ImageField(default='book.jpg')

    def __str__(self):
        return f'{self.title}'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    def __str__(self):
        return f'{self.first_name}  {self.last_name}'

    def full_name(self):
        return f'{ self.first_name } { self.last_name }'

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.title} BY {self.author}'



class BookReview(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    starts_given = models.IntegerField(
        validators=[MinValueValidator(-5),MaxValueValidator(5)]
    )

    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.starts_given} || {self.user.username}'
