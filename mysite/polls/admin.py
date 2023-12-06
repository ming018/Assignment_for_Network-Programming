from django.contrib import admin
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin) :
    field = ['pub_date', 'question_text']

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)