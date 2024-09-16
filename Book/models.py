from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    books = models.ManyToManyField(Book,related_name='publisher')
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5
    comment = models.TextField()
    
    