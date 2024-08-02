from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateTimeField()
# Create your models here.

class Professor(models.Model):
    nome= models.CharField(max_length=200)

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    #chave estrangeira para Curso.
    curso= models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor= models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    nome= models.CharField(max_length=200)
    codigo = models.CharField(max_length=6, null=True)
    
    #definindo uma relacao muitos para muitos
    alunos= models.ManyToManyField(Aluno)

class Matricula (models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete= models.CASCADE)
    periodo = models.IntegerField(null=True)
    
    
#item 2 exiba todos os alunos associados a disciplina
# for disciplina in lista_disciplina:
    #lista_alunos_disciplina= disciplina.alunos.all()
    #print(f'Disciplina: {disciplina}, Alunos: {lista_alunos_disciplina}')
    
#exita todos as disciplinas associadas ao aluno
#for alunos in lista_alunos
    # aluno=
