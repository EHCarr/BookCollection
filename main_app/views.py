from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import QuoteForm
class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'read']

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'age']

class BookDelete(DeleteView):
    model = Book
    fields = ['title', 'author', 'description', 'age']
    success_url = '/books/'
    
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def books_detail(request, book_id):
    #SELECT * FROM main_app_book WHERE id = book_id
    book = Book.objects.get(id = book_id)
    # return render(request, 'books/detail.html', {'book': book})
    quote_form = QuoteForm()
    return render(request, 'books/detail.html', {'book': book, 'quote_form': quote_form})

def add_quote(request, book_id):
    form = QuoteForm(request.POST)
    
    if form.is_valid():
        new_quote = form.save(commit=False)
        new_quote.book_id = book_id
        new_quote.save()
    return redirect('detail', book_id = book_id)

