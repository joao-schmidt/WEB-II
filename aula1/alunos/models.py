from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateTimeField("data punlished")
# Create your models here.
