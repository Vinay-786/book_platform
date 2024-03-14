from django.shortcuts import render
from .models import Book

def index(request):
    context = {
        "book7": Book.objects.get(pk=7).file_upload.url,
        "book6": Book.objects.get(pk=6).file_upload.url,
        "book5": Book.objects.get(pk=5).file_upload.url,
        "book4": Book.objects.get(pk=4).file_upload.url,
        "book3": Book.objects.get(pk=3).file_upload.url,
        "book2": Book.objects.get(pk=2).file_upload.url,
            }

    return render(request, 'main/index.html', context)


def readmore(request, book_id):
    books = Book.objects.get(pk=book_id)
    return render(request, "readmoreTempl/readmore.html",{
        "books": books
        })

def explore(request):
    books = Book.objects.all()
    return render(request, "main/explore.html", {
        "books": books
        })

def ItEndsWithUs(request):
    return render(request, 'readmoreTempl/ItEndsWithUs.html')



