from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Utilisateurs (models.Model):
    #id = models.IntegerField(unique = True )
    nom = models.CharField (max_length = 200)
    status = models.CharField (max_length = 30)
    mot_de_passe = models.CharField(max_length = 20, unique = True)

    class Meta:
        db_table = 'Utilisateurs'
        """managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames' """