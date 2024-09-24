from django.contrib import admin
from .models import Book, Author, Publisher, Genre, Loan, Borrower, Review

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Loan)
admin.site.register(Borrower)
admin.site.register(Review)