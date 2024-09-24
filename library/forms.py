from django import forms
from .models import Review, Author, Publisher, Genre, Borrower, Book, Loan

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']