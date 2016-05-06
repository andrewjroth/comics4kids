from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from comics import models

class HomePageView(TemplateView):
    template_name = "comics/home.html"

class BookList(ListView): # template: 'comics/book_list.html'
    model = models.Book

class BookDetail(DetailView):
    model = models.Book
