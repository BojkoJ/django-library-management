from django import forms
from .models import Review, Author, Publisher, Genre, Borrower, Book, Loan

# Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']










"""
# Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
        # Form for submitting a review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'reviewer_name', 'rating']
        widgets = {
            'book': forms.HiddenInput(),  # Hide the book field in the form
        }

# Form for submitting an author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

# Form for submitting a publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

# Form for submitting a genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Form for submitting a borrower
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name']

# Form for submitting a book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'genre']

# Form for submitting a loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'borrower', 'date_borrowed', 'return_date']
"""