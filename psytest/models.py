from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    scales = models.JSONField(default=dict)
    interpretations = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    answer = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answers = models.JSONField(default=list)
    result = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.test}"



