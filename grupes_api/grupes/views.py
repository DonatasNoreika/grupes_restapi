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
                          AlbumReviewLikeSerializer,
                          AllAlbumReviewSerializer,
                          UserSerializer)

from rest_framework.exceptions import ValidationError
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from django.contrib.auth.models import User


class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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
        album = Album.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album=album)

    def get_queryset(self):
        album = Album.objects.get(pk=self.kwargs['pk'])
        return AlbumReview.objects.filter(album=album)


class AllAlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AllAlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        comment = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if comment.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima trinti svetimų komentarų!')

    def put(self, request, *args, **kwargs):
        comment = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if comment.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima koreguoti svetimų komentarų!')


class AlbumReviewCommentList(generics.ListCreateAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_review=album_review)

    def get_queryset(self):
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewComment.objects.filter(album_review=album_review)


class AlbumReviewLikeList(generics.CreateAPIView, mixins.DestroyModelMixin):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('Jūs jau palikote patiktuką šiam pranešimui!')
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_review=album_review)

    def get_queryset(self):
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewComment.objects.filter(album_review=album_review)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('Jūs nepalikote patiktuko po šiuo pranešimu!')

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )