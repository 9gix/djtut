from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.book_list,
        name='book-list'),
    url(r'^(?P<book_id>\d+)/$', views.book_detail,
        name='book-detail'),
]
