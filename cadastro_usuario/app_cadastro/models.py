from django.db import models

class Usuario(models.Model):  # Certifique-se de que o nome da classe corresponde ao usado em suas migrações/views.
    id_usuario = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    renda_mensal = models.DecimalField(max_digits=15, decimal_places=2)
    credito = models.FloatField(default=0.0)  # Este campo deve estar presente