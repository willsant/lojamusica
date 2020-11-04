from django.db import models
from django.conf import settings

class Instrumento(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='operacoes_do_usuario',
                             on_delete=models.DO_NOTHING,
                             null=True)
    nome = models.CharField(max_length=200, db_index=True)
    descricao = models.CharField(max_length=200, db_index=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.descricao

# Create your models here.
