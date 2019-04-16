# from django.db import models
# from django.utils import timezone
#
# class TagManager(Models.Manager):
#     pass
#
# class QuestionManager(Models.Manager):
#     pass
#
# class AnswerManager(Models.Manager):
#     pass
#
#
# class Tag(models.Model):
#     name = models.CharField(max_length=20, default="404", verbose_name="Question's Tag")
#
#     objects = TagManager()
# 
#     def __str__(self):
#         return self.name
#
#
# class Question(models.Model):
#     author = models.ForeignKey(User, verbose_name="Question's Owner")
#     title = models.CharField(max_length=50, verbose_name="Question's Header")
#     text = models.TextField(verbose_name="Question's Content")
#     date = models.DateTimeField(default=timezone.now, verbose_name="Question's Date")
#     rating = models.IntegerField(default=0, null=False, verbose_name="Question's Rating")
#     is_active = models.BooleanField(default=True, verbose_name="Question's Availability")
#     tags = models.ManyToManyField(Tag, default=True, related_name='questions', verbose_name="Question's Tags")
#
#     objects = QuestionManager()
#
#     def __str__(self):
#         return self.text
#
#
# class Answer(models.Model):
#     author = models.ForeignKey(User, verbose_name="Answer's Owner")
#     date = models.DateTimeField(default=timezone.now, verbose_name="Answer's Date")
#     question = models.ForeignKey(Question, related_name='answers', verbose_name="Answer's Question")
#     text = models.TextField(verbose_name="Answer's Content")
#     rating = models.IntegerField(default=0, null=False, verbose_name="Answer's Rating")
#
#
#     objects = AnswerManager()
#
#     def __str__(self):
#         return self.text
