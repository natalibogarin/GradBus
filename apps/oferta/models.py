from django.db import models

# Create your models here.
class Oferta(models.Model):
	id = models.IntegerFields()
	titulo = models.CharFields(max_length = 100)
	fecha = models.DateField(auto_now=True, auto_now_add=True)
	descripcion = models.TextFields()
	requisitos = models.TextFields()
	lugardetrabajo = models.CharFields(max_length=100)
	beneficios = models.TextFields(null=True)

		