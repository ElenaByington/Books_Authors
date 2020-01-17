from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index),

    path('new_book', views.add_new_book),
    path('books/<int:id>', views.book_page),
    path('<int:id>/select_author', views.select_author),

    path('authors', views.author),

    path('new_author', views.add_new_author),
    path('authors/<int:id>', views.author_page),
    path('<int:id>/select_book', views.select_book),

]
