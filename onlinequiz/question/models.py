from django.db import models

# Create your models here.
class Question(models.Model):
    topic = models.CharField(max_length=255)
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    level=models.CharField(max_length=100,null=True)