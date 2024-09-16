from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.title
       
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    books = models.ManyToManyField(Book,related_name='publisher')
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.book.title} - {self.rating}/5"
    
    