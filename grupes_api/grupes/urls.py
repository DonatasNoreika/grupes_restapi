from django.contrib import admin
from django.urls import path, include
from .views import (BandList,
                    AlbumList,
                    SongList,
                    AlbumReviewList,
                    AlbumReviewCommentList,
                    AlbumReviewLikeList,
                    BandDetail,
                    AlbumDetail,
                    AllAlbumReviewList,
                    AlbumReviewDetail)

urlpatterns = [
    path('bands', BandList.as_view()),
    path('bands/<int:pk>', BandDetail.as_view()),
    path('albums', AlbumList.as_view()),
    path('bands/<int:pk>', AlbumDetail.as_view()),
    path('songs', SongList.as_view()),
    path('album_reviews', AllAlbumReviewList.as_view()),
    path('album_reviews/<int:pk>', AlbumReviewDetail.as_view()),
    path('albums/<int:pk>/reviews', AlbumReviewList.as_view()),
    path('album_review_comments', AlbumReviewCommentList.as_view()),
    path('album_review_likes', AlbumReviewLikeList.as_view()),
]
