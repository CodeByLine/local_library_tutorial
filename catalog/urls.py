from django.urls import path
from . import views
from django.views import generic

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('authors', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

]
