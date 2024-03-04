from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        path("", views.index, name='index'),
        path("explore/<int:book_id>", views.readmore, name='readmore'),
        path("explore", views.explore, name='explore'),
        path("ItEndsWithUs", views.ItEndsWithUs, name='ItEndsWithUs'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
