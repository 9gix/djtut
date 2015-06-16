from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('book', views.BookViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls, namespace='bookapi'), name='book-api'),
    url(r'^$', views.book_list,
        name='book-list'),
    url(r'^(?P<book_id>\d+)/$', views.book_detail,
        name='book-detail'),
    url(r'^search/$', views.search,
        name='book-search'),
    url(r'^intro-python/$', views.intro_python,
        name='intro-python'),
]
