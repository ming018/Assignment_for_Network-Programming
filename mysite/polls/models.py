from django.db import models

# Create your models here.

class Question(models.Model) :
    # 기본적인 pk인 id 도 같이 있음
    question_text = models.CharField(max_length = 200) # 
    pub_date = models.DateTimeField('date published')

    def __str__(self) : # 이 함수를 통해서 어드민 페이지에서 테이블을 손쉽게볼 수 있음
        return self.question_text
    
class Choice(models.Model) :
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self) :
        return self.choice_text