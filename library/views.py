from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Publisher, Loan, Genre, Borrower, Publisher, Review
from django.db.models import Count, Avg, Func
from django.utils import timezone
from django.db.models.functions import Round
from .forms import ReviewForm, AuthorForm, PublisherForm, GenreForm, BorrowerForm, BookForm, LoanForm


class Round(Func):
    function = 'ROUND'
    arity = 1  # Set the arity to 1 since the ROUND function only takes one argument

def book_list(request):
    # Annotate each book queryset with its average rating rounded to the nearest integer
    books = Book.objects.annotate(average_rating=Round(Avg('review__rating')))
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    loans = Loan.objects.filter(book=book)
    borrowers = [loan.borrower for loan in loans]
    
    reviews = Review.objects.filter(book=book)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    # Kontrola, zda je průměrné hodnocení rovno None
    if average_rating is None:
        average_rating = 0  # Nastavit na nulu nebo jinou výchozí hodnotu
    
    print(average_rating)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            # Přesměrování zpět na detail knihy po přidání recenze
            return redirect('book_detail', book_id=book_id)
    else:
        form = ReviewForm()

    return render(request, 'book_detail.html', {'book': book, 'borrowers': borrowers, 'reviews': reviews, 'average_rating': average_rating, 'review_form': form})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author)
    publishers = Publisher.objects.filter(book__author=author).distinct()
    return render(request, 'author_detail.html', {'author': author, 'books': books, 'publishers': publishers})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    books = Book.objects.filter(genre=genre)
    return render(request, 'genre_detail.html', {'genre': genre, 'books': books})

def loan_list(request):
    today = timezone.now().date()
    loans = Loan.objects.all()
    return render(request, 'loan_list.html', {'loans': loans, 'today': today})

def loan_detail(request, loan_id):
    # Získáme konkrétní vypůjčku podle jejího ID
    loan = get_object_or_404(Loan, pk=loan_id)
    today = timezone.now().date()
    return render(request, 'loan_detail.html', {'loan': loan, 'today': today})

def borrower_list(request):
    borrowers = Borrower.objects.all()
    return render(request, 'borrower_list.html', {'borrowers': borrowers})

def borrower_detail(request, borrower_id):
    borrower = get_object_or_404(Borrower, pk=borrower_id)
    loans = Loan.objects.filter(borrower=borrower).select_related('book__author', 'book__publisher')
    borrowed_books = [loan.book for loan in loans]
    return render(request, 'borrower_detail.html', {'borrower': borrower, 'borrowed_books': borrowed_books})

def publisher_list(request):
    # Získat všechny vydavatele a spočítat počet knih pro každého vydavatele
    publishers = Publisher.objects.annotate(num_books=Count('book'))
    return render(request, 'publisher_list.html', {'publishers': publishers})

def publisher_detail(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    books = Book.objects.filter(publisher=publisher)
    return render(request, 'publisher_detail.html', {'publisher': publisher, 'books': books})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book_id = form.cleaned_data['book_id']  # Použití 'book_id' místo 'book'
            review.save()
            # Přesměrování na detail knihy, která byla ohodnocena
            return redirect('book_detail', book_id=review.book_id)
    else:
        form = ReviewForm()
    return render(request, 'book_detail.html', {'form': form})

def author_create_view(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  
    else:
        form = AuthorForm()
    return render(request, 'author_create_view.html', {'form': form})

def publisher_create_view(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')  

    else:
        form = PublisherForm()
    return render(request, 'publisher_create_view.html', {'form': form})



def genre_create_view(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')    
    else:
        form = GenreForm()
    return render(request, 'genre_create_view.html', {'form': form})


def borrower_create_view(request):
    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrower_list')     
    else:
        form = BorrowerForm()
    return render(request, 'borrower_create_view.html', {'form': form})

def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  
    else:
        form = BookForm()
        
    # Získání seznamu autorů a vydavatelů pro použití ve formuláři
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    genres = Genre.objects.all()
    
    return render(request, 'book_create_view.html', {'form': form, 'authors': authors, 'publishers': publishers, 'genres': genres})

def loan_create_view(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loan_list')  # Přizpůsobte podle vaší aplikace
    else:
        form = LoanForm()
        
    # Získání seznamu knih a vypůjčovatelů pro použití ve formuláři
    books = Book.objects.all()
    borrowers = Borrower.objects.all()
    
    return render(request, 'loan_create_view.html', {'form': form, 'books': books, 'borrowers': borrowers})