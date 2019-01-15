from django.shortcuts import render , redirect
from .models import BookList
# Create your views here.
def index(request):
    books = BookList.objects.all()
    return render(request,'index.html',{'books':books})
def edit(request,id):
    books=BookList.objects.get(id=id)
    context={'books':books}
    return render(request,'edit.html',context)

def update(request,id):
    books=BookList.objects.get(id=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('/')

def delete(request,id):
    books=BookList.objects.get(id=id)
    books.delete()
    return redirect('/')

def add_book(request):
  return render(request,'add_book.html')

def create(request):
    title=request.GET['title']
    price=request.GET['price']
    author=request.GET['author']
    new_book=BookList(title=title,price=price,author=author)
    new_book.save()
    return redirect('/')

