from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)  # Použijeme ID žánru "Nezařazeno"

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Loan(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    borrower = models.ForeignKey('Borrower', on_delete=models.CASCADE)
    date_borrowed = models.DateField()
    return_date = models.DateField()

class Borrower(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Bodové hodnocení od 1 do 5

    def __str__(self):
        return f"Review of {self.book.title} by {self.reviewer_name}"

