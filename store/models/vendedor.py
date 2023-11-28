from django.db import models


class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome + ' - ' + self.email
