from django.contrib import admin
from question.models import Question, Tag, User, Answer, LikeDislike

# Register your models here.

# Username: admin
# Password: adminadmin

admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Answer)
admin.site.register(LikeDislike)
