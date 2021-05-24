from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)


class Album(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)
    band = models.ForeignKey('Band', on_delete=models.CASCADE)


class Song(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)
    duration = models.IntegerField(verbose_name="Duration")
    band = models.ForeignKey('Band', verbose_name="Band", on_delete=models.CASCADE)


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey('Album', verbose_name="Album", on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    score = models.CharField(verbose_name="Score", max_length=50)


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review = models.ForeignKey('AlbumReview', verbose_name="Album Review", on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review = models.ForeignKey('AlbumReview', verbose_name="Album Review", on_delete=models.CASCADE)
