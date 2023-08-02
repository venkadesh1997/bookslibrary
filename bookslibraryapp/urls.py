from django.urls import path
from . import views
app_name='bookslibraryapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('books/<int:books_id>/',views.detail,name='detail'),
    path('add/',views.add_books,name='add_books'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]

