from django.db import models
from django.contrib.auth.models import User


class company(models.Model):
    name = models.CharField(max_length=20)
    users = models.ManyToManyField(User)
    def __str__(self):
        return self.name

class toDoList(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=100)
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name




