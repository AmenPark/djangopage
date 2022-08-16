from django.db import models

class Problem(models.Model):
    subject = models.CharField(max_length = 40)
    content = models.TextField()
    create_date = models.DateTimeField()

class Solution(models.Model):
    Problem = models.ForeignKey(Problem, on_delete= models.CASCADE)     # 질문 삭제시 답변도 삭제. CASCADE의 의미.
    content = models.TextField()
    create_date = models.DateTimeField()


# Create your models here.
