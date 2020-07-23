#from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Declaration(models.Model):
    regime = models.CharField(max_length=4)
    produit = models.CharField(max_length=10)
    mode_cond=models.CharField(max_length=4)
    origine=models.CharField(max_length=3)
    provenance=models.CharField(max_length=4)
    valeur_caf=models.IntegerField()
    poids_net=models.IntegerField()
    destinataire=models.CharField(max_length=7)
    declarant=models.CharField(max_length=7)
    mode_paiement=models.IntegerField()
#    circuit=models.CharField(max_length=1)

    
