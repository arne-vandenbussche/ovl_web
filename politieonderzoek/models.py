from django.db import models

class Politieterm(models.Model):
    afkorting = models.CharField(unique=True)
    betekenis = models.CharField()
    uitleg = models.CharField(blank=True)
    
class Auto(models.Model):
    nummerplaat = models.CharField(unique=True)
    autotype = models.CharField()
    kleur = models.CharField()
    opmerkingen = models.CharField(blank=True)
    
class Persoon(models.Model):
    voornaam = models.CharField()
    familienaam = models.CharField()
    beroep = models.CharField()
    opmerkingen = models.CharField(blank=True)