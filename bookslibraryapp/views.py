from django.http import HttpResponse
from django.shortcuts import render, redirect

from . models import Books
from . forms import BooksForm

# Create your views here.
def index(request):

   books=Books.objects.all()
   context={
       'books_list':books
   }
   return render(request,'index.html',context)
def detail(request,books_id):
    books=Books.objects.get(id=books_id)
    return render(request,"detail.html",{'books':books})

def add_books(request):
    if request.method =="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        books=Books(name=name,desc=desc,year=year,img=img)
        books.save()

    return render(request,'add.html')

def update(request,id):
    books=Books.objects.get(id=id)
    form=BooksForm(request.POST or None,request.FILES,instance=books)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'books':books})

def delete(request,id):
    if request.method=='POST':
        books=Books.objects.get(id=id)

        books.delete()
        return redirect('/')

    return render(request,'delete.html')