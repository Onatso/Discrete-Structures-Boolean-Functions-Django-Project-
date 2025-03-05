from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)



Difficult_choices = [
    ('Лёгкий', 'Easy'),
    ('Средний', 'Middle'),
    ('Сложный', 'Different')
]

class Task(models.Model):
    author = models.ForeignKey(Teacher,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=255)
    description = models.TextField(unique=True,null = False,default="Образец")
    level = models.CharField(choices= Difficult_choices,default='Лёгкий',max_length=8)


    def get_absolute_url(self):
        return str(self.id)

    def __str__(self):
        return f'Задача "{self.title}"'







