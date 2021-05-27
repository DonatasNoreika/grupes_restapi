from rest_framework import serializers
from .models import (Band,
                     Album,
                     Song,
                     AlbumReview,
                     AlbumReviewComment,
                     AlbumReviewLike)
from django.contrib.auth.models import User


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name', 'image']


class AlbumSerializer(serializers.ModelSerializer):
    band_name = serializers.StringRelatedField(source='band.name')

    class Meta:
        model = Album
        fields = ['id', 'band_name', 'band', 'name']


class SongSerializer(serializers.ModelSerializer):
    band_name = serializers.ReadOnlyField(source='band.name')

    class Meta:
        model = Song
        fields = ['id', 'band', "band_name", 'name', 'duration', ]


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album = serializers.ReadOnlyField(source='album.id')
    album_name = serializers.ReadOnlyField(source='album.name')

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_id', 'album_name', 'album', 'content', 'score']


class AllAlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_name = serializers.ReadOnlyField(source='album.name')
    comments = serializers.StringRelatedField(many=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_id', 'album_name', 'album', 'content', 'score', 'comments', 'likes_count']

    def get_likes_count(self, obj):
        return AlbumReviewLike.objects.filter(album_review=obj).count()


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_review = serializers.ReadOnlyField(source='album_review.id')

    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'user', 'user_id', 'album_review', 'content']


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_review = serializers.ReadOnlyField(source='album_review.id')

    class Meta:
        model = AlbumReviewLike
        fields = ['id', 'user', 'user_id', 'album_review']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user