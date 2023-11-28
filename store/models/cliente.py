from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome + ' - ' + self.email
