from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Book.views import AuthorViewSet, BookViewSet, PublisherViewSet, ReviewViewSet
from django.contrib import admin


from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'publisher', PublisherViewSet, basename='publisher')
router.register(r'review', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]