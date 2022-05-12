from django.contrib import admin
from .models import Book,Author,BookReview,BookAuthor
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title','isbn')
    list_display = ('title','isbn','description',)

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name','last_name',)

class BookReviewAdmin(admin.ModelAdmin):
    search_fields = ('user','book',)

class BookAuthorAdmin(admin.ModelAdmin):
    search_fields = ('book','author',)

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(BookReview,BookReviewAdmin)
admin.site.register(BookAuthor,BookAuthorAdmin)
