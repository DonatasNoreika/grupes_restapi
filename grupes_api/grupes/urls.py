from django.contrib import admin
from django.urls import path, include
from .views import (BandList,
                    AlbumList,
                    SongList,
                    AlbumReviewList,
                    AlbumReviewCommentList,
                    AlbumReviewLikeList,
                    BandDetail,
                    AlbumDetail)

urlpatterns = [
    path('bands', BandList.as_view()),
    path('bands/<int:pk>', BandDetail.as_view()),
    path('albums', AlbumList.as_view()),
    path('bands/<int:pk>', AlbumDetail.as_view()),
    path('songs', SongList.as_view()),
    path('album_reviews', AlbumReviewList.as_view()),
    path('album_review_comments', AlbumReviewCommentList.as_view()),
    path('album_review_likes', AlbumReviewLikeList.as_view()),
]
