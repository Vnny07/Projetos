from django.db import models

class Usuario(models.Model):
    usu_nome = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    usu_email = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

class Tarefa(models.Model):
    tar_descricao = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    tar_setor = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    tar_prioridade = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    tar_status = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    tar_data = models.DateField(
        null=True,
        blank=True
    )
    usu_codigo = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    objetos = models.Manager()