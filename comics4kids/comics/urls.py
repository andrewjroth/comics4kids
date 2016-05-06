from django.conf.urls import url

from comics import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^books$', views.BookList.as_view(), name='book-list'),
    url(r'^books/(?P<pk>[\d]+)$', views.BookDetail.as_view(), name='book-detail')
]
