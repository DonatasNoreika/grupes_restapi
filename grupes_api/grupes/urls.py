from django.contrib import admin
from django.urls import path, include
from .views import (BandList,
                    AlbumList,
                    SongList)


urlpatterns = [
    path('bands', BandList.as_view()),
    path('albums', AlbumList.as_view()),
    path('songs', SongList.as_view()),
]
