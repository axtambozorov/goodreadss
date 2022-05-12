from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from books.forms import BookReviewForm
from books.models import Book, BookReview
from django.views.generic import ListView,DetailView

# class Booksview(ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = 'books'
#     paginate_by = 2

class  Booksview(View):
    def get(self,request):
        books =Book.objects.all().order_by('id')
        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains = search_query)
        paginator = Paginator(books,2)
        page_num = request.GET.get('page',1)
        page_obj = paginator.get_page(page_num)

        return render(request,'books/list.html',{'page_obj':page_obj })

# class BooksDetailView(DetailView):
#     template_name = 'books/detail.html'
#     pk_url_kwarg = 'id'
#     model = Book


class BooksDetailView(View):
    def get(self,request,id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm
        return render(request, 'books/detail.html', { "book":book,'review_form':review_form } )

class AddReviewBook(LoginRequiredMixin, View):
    def post(self,request,id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)
        if review_form.is_valid():
            BookReview.objects.create(
                user=request.user,
                book=book,
                comment = review_form.cleaned_data['comment'],
                starts_given = review_form.cleaned_data['starts_given']
            )
            return redirect(reverse('books:detail', kwargs={'id':book.id}))
        return render(request, 'books/detail.html', {"book": book, 'review_form': review_form})


