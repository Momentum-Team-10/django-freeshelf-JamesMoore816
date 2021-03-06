"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from books import views as books_views

urlpatterns = [
    path("", books_views.home, name = 'home'),
    path("admin/", admin.site.urls),
    path('accounts/favorites/', books_views.favorites_page, name = 'favorites_page'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('books/add/', books_views.add_book, name='add_book'),
    path('books/<slug:slug>/', books_views.view_book, name='view_book'),
    path('books/<slug:slug>/edit/', books_views.edit_book, name='edit_book'),
    path('books/<slug:slug>/delete/', books_views.delete_book, name='delete_book'),
    path('categories/<slug:slug>/', books_views.category_search, name='category_search'),
]
