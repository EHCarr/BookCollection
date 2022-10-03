from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 150)
    author = models.CharField(max_length= 150)
    description = models.CharField(max_length = 1000)
    read = models.BooleanField(default='None')
    image = models.ImageField(upload_to='main_app/static/uploads/', default='no image')

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'book_id': self.id})

    def __str__(self):
        return self.title
    
class Quote(models.Model):
    date = models.DateField()
    page = models.CharField(max_length=100)
    quote = models.CharField(max_length= 1000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self): 
       return f"{self.get_quote_on_display()} on {self.date}" 

   

