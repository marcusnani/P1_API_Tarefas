from django.db import models
from usuarios.models import Usuario  # O import fica aqui no topo!

class Tarefa(models.Model):
    status_choices = [
        ("ABERTA", "Aberta"),
        ("CANCELADA", "Cancelada"),
        ("CONCLUIDA", "Concluída"),
    ]

    prioridade_choices = [
        ("URGENTE", "Urgente"),
        ("NAO_URGENTE", "Não urgente")
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=status_choices, default="ABERTA")
    prioridade = models.CharField(max_length=20, choices=prioridade_choices, default="NAO_URGENTE")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    
    # O campo novo que conecta com Usuário:
    usuario_responsavel = models.ForeignKey(
        Usuario, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.titulo