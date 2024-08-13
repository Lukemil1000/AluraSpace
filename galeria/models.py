from django.db import models

class Fotografia(models.Model):

    nome = models.CharField(null=False, blank=False, max_length=100)
    legenda = models.CharField(null=False, blank=False, max_length=150)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self) -> str:
        return self.nome