from django.db import models

# 질문
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

# 보기
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # CASCADE 주체가 없어지면 ForeignKey도 없어 지겠다
                      #class Question 노예,종?
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        #object입력값이 나오는 게아니라 입력값만 문자열로 나오게 하기위해