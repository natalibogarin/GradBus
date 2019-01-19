from django.db import models

# Create your models here.
class Rubro(models.Model):
	id = models.IntegerFields()
	nomb = models.CharFields(max_length=50)


