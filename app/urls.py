# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('products', views.products, name='products'),
    path('addProduct', views.addProduct, name='addProduct'),
    path('categories', views.categories, name='categories'),
    path('addCategory', views.addCategory, name='addCategory'),
    path('reviews', views.reviews, name='reviews'),
    path('addReview', views.addReview, name='addReview'),
    path('users', views.users, name='users'),
    path('addUser', views.addUser, name='addUser'),

]
