from django.urls import path
from library.views import book_list, book_detail, author_list, author_detail, genre_list, genre_detail, loan_list, loan_detail, borrower_list, borrower_detail, publisher_list, publisher_detail, add_review, author_create_view, publisher_create_view, genre_create_view, borrower_create_view, book_create_view, loan_create_view
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('authors/', author_list, name='author_list'),
    path('authors/<int:author_id>/', author_detail, name='author_detail'),
    path('genres/', genre_list, name='genre_list'),
    path('genres/<int:genre_id>/', genre_detail, name='genre_detail'),
    path('loans/', loan_list, name='loan_list'),
    path('loans/<int:loan_id>/', loan_detail, name='loan_detail'),
    path('borrowers/', borrower_list, name='borrower_list'),
    path('borrowers/<int:borrower_id>/', borrower_detail, name='borrower_detail'),
    path('publishers/', publisher_list, name='publisher_list'),
    path('publishers/<int:publisher_id>/', publisher_detail, name='publisher_detail'),
    path('add_review/', add_review, name='add_review'),
    path('add_author/', author_create_view, name='author_create_view'),
    path('add_publisher/', publisher_create_view, name='publisher_create_view'),
    path('add_genre/', genre_create_view, name='genre_create_view'),
    path('add_borrower/', borrower_create_view, name='borrower_create_view'),
    path('add_book/', book_create_view, name='book_create_view'),
    path('add_loan/', loan_create_view, name='loan_create_view')
]