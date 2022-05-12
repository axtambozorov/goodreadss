from django.test import TestCase
from django.urls import reverse

from books.models import Book, BookReview
from users.models import CustomUser


class HomePageTestCase(TestCase):
    def test_paginated_list(self):
        user = CustomUser.objects.create(username='user',first_name='firstname',last_name='lastname',email='email')
        book = Book.objects.create(title='book1',description ='description',isbn='123456789')

        review1 = BookReview.objects.create(user=user,book=book,comment='very good book',starts_given='3')
        review2 = BookReview.objects.create(user=user,book=book,comment='nice book',starts_given='4')
        review3 = BookReview.objects.create(user=user,book=book,comment='useful book',starts_given='5')
        review4 = BookReview.objects.create(user=user,book=book,comment='good',starts_given='3')
        review5 = BookReview.objects.create(user=user,book=book,comment='nice',starts_given='4')



        response = self.client.get(reverse('home'))

        self.assertContains(response, review5.comment)
        self.assertContains(response, review4.comment)
        self.assertNotContains(response, review3.comment)
        self.assertContains(response, review2.comment)
        # self.assertContains(response, review1.comment)