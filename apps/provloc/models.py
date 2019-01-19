from django.db import models

# Create your models here.
class Provincia(models.Model):
	id = models.IntegerFields()
	nomb = models.CharFields(max_length=50)

class Localidad(models.Model):
	id = models.IntegerFields()
	nomb = models.CharFields(max_length=50)