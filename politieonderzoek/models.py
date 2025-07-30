from django.db import models

class Politieterm(models.Model):
    afkorting = models.CharField(unique=True)
    betekenis = models.CharField()
    uitleg = models.CharField(blank=True)

    def __str__(self):
        return f"{self.afkorting} - {self.betekenis}"


class Auto(models.Model):
    nummerplaat = models.CharField(unique=True)
    autotype = models.CharField()
    kleur = models.CharField()
    opmerkingen = models.CharField(blank=True)

    def __str__(self):
            return f"{self.nummerplaat} ({self.autotype}, {self.kleur})"


class Persoon(models.Model):
    voornaam = models.CharField()
    familienaam = models.CharField()
    geboortedatum = models.CharField(default="00/00/0000")
    beroep = models.CharField()
    opmerkingen = models.CharField(blank=True)

    def __str__(self):
        return f"{self.voornaam} {self.familienaam}"
