import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Question(models.Model):
     question_text = models.CharField(max_length = 200);# las preguntas al usuario
     pub_date  = models.DateTimeField("date published");

     def __str__(self):
        return self.question_text # con esto le digo que me muestre el valor de question_text en letras
          
     def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# Segundo modelo

class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE);
    choice_text = models.CharField(max_length = 200);# son las respuestas a la preguntas
    votes = models.IntegerField(default = 0);


    def __str__(self):
        return self.choice_text # con esto le digo que me muestre el valor de choice_text en letras
