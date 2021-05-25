from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import generics, permissions
from .models import (Band,
                     Album,
                     Song,
                     AlbumReview,
                     AlbumReviewComment,
                     AlbumReviewLike)
from .serializers import (BandSerializer,
                          AlbumSerializer,
                          SongSerializer,
                          AlbumReviewSerializer,
                          AlbumReviewCommentSerializer,
                          AlbumReviewLikeSerializer)

from rest_framework.exceptions import ValidationError

class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def delete(self, request, *args, **kwargs):
    #     post = Band.objects.filter(pk=kwargs['pk'], user=self.request.user)
    #     if post.exists():
    #         return self.destroy(request, *args, **kwargs)
    #     else:
    #         raise ValidationError('Negalima trinti svetimų pranešimų!')
    #
    # def put(self, request, *args, **kwargs):
    #     post = Band.objects.filter(pk=kwargs['pk'], user=self.request.user)
    #     if post.exists():
    #         return self.update(request, *args, **kwargs)
    #     else:
    #         raise ValidationError('Negalima koreguoti svetimų pranešimų!')

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewCommentList(generics.ListCreateAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewLikeList(generics.ListCreateAPIView):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
