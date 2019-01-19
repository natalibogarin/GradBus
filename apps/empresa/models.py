from django.db import models

# Create your models here.
class Empresa(models.Model):
	razsoc = models.CharFields(max_lenght=50)
	mail = models.EmailFields(max_lenght=254)
	telef = models.IntegerFields()
	dire = models.CharFields(max_lenght=200, null=True)
	logo = models.ImageFields(upload_to="logos", null=True)
