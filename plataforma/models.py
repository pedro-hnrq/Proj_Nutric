from django.db import models
from django.contrib.auth.models import User


class Pacientes(models.Model):
    objects = None
    choices_sexo = (('F', 'Feminino'),
                    ('M', 'Maculino'))
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    nutri = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class DadosPaciente(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    data = models.DateTimeField()
    peso = models.FloatField()
    altura = models.FloatField()
    percentual_gordura = models.FloatField()
    percentual_musculo = models.FloatField()
    colesterol_hdl = models.FloatField()
    colesterol_ldl = models.FloatField()
    colesterol_total = models.FloatField()
    trigliceridios = models.FloatField()

    def __str__(self):
        return f"Paciente({self.paciente.nome}, {self.peso})"
