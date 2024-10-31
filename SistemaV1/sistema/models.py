from django.db import models

class TblUsuarios(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    username = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    senha = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )

    objetos = models.Manager()