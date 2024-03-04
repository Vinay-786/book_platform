from django.shortcuts import render
from .models import Book

def index(request):
    return render(request, 'main/index.html')


def readmore(request, book_id):
    books = Book.object.get(pk=book_id)
    return render(request, "readmoreTempl/readmore.html",{
        "book": books
        })

def explore(request):
    books = Book.objects.all()
    return render(request, "main/explore.html", {
        "books": books
        })

def ItEndsWithUs(request):
    return render(request, 'readmoreTempl/ItEndsWithUs.html')



