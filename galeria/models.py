from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField(null=False, blank=False, max_length=100)
    legenda = models.CharField(null=False, blank=False, max_length=150)
    categoria = models.CharField(default="", max_length=100, choices=OPCOES_CATEGORIA)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(blank=False, upload_to="fotos/%Y/%m/%d")
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now(), blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self) -> str:
        return self.nome