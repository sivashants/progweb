from django.db import models

# Create your models here.
class Categorie(models.Model):
	nom = models.CharField(max_length=30)
	def __unicode__(self):
		return u"%s" % self.nom

class Movie(models.Model):
	titre = models.CharField(max_length=100)
	realisateur = models.CharField(max_length=42)
	resume = models.TextField(null=True)
	release_date=models.DateField(verbose_name="Date de sortie")
	categorie = models.ForeignKey('Categorie')

	def __unicode__(self):
		return u"%s" % self.titre


