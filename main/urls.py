from django.urls import path 
from . import views

urlpatterns = [
        path("", views.index, name='index'),
        path("explore/<int:book_id>", views.readmore, name='readmore'),
        path("explore", views.explore, name='explore'),
        path("ItEndsWithUs", views.ItEndsWithUs, name='ItEndsWithUs'),
] 
