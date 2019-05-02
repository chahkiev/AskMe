from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
# from PIL import Image, ExifTags

from question.managers import UserManager, TagManager, QuestionManager, AnswerManager, LikeDislikeManager


# AUTH_USER_MODEL set in settings
class User(AbstractUser):
    upload = models.ImageField(default="media/default/default_avatar.png", upload_to="uploads/%Y/%m/%d/", verbose_name="User's Avatar")
    registration_date = models.DateTimeField(default=timezone.now, verbose_name="User's Registration Date")
    rating = models.IntegerField(default=0, verbose_name="User's Rating")

    objects = UserManager()

    def __str__(self):
        return self.username


class Tag(models.Model):
    name = models.CharField(max_length=20, default="404", verbose_name="Question's Tag")

    objects = TagManager()

    def __str__(self):
        return self.name


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Dislike'),
        (LIKE, 'Like')
    )

    vote = models.SmallIntegerField(verbose_name=("Vote"), choices=VOTES)
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()

    def __str__(self):
        return self.user.username + " liked"


class Question(models.Model):
    author = models.ForeignKey(User, verbose_name="Question's Owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="Question's Header")
    text = models.TextField(verbose_name="Question's Content")
    date = models.DateTimeField(default=timezone.now, verbose_name="Question's Date")
    rating = models.IntegerField(default=0, null=False, verbose_name="Question's Rating")
    is_active = models.BooleanField(default=True, verbose_name="Question's Availability")
    tags = models.ManyToManyField(Tag, default=True, related_name='questions', verbose_name="Question's Tags")
    votes = GenericRelation(LikeDislike, related_query_name='questions')

    objects = QuestionManager()

    def __str__(self):
        return self.text


class Answer(models.Model):
    author = models.ForeignKey(User, verbose_name="Answer's Owner", on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, verbose_name="Answer's Date")
    question = models.ForeignKey(Question, related_name='answers', verbose_name="Answer's Question", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Answer's Content")
    rating = models.IntegerField(default=0, null=False, verbose_name="Answer's Rating")
    votes = GenericRelation(LikeDislike, related_query_name='answers')

    objects = AnswerManager()

    def __str__(self):
        return self.text
