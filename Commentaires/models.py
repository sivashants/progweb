from django.db import models
from django.contrib.auth.models import User
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

class Serie(models.Model):
	titre = models.CharField(max_length=100)
	realisateur=models.CharField(max_length=42)
	resume=models.TextField(null=True)
	seasons=models.IntegerField() 
	Completed=models.BooleanField()
	def __unicode__(self):
		return u"%s" % self.titre

class Movie_Comments(models.Model):
	titre = models.CharField(max_length=100)
	contenu = models.TextField(null=False)
	author= models.ForeignKey(User)
	def __unicode__(self):
		return u"%s" % self.titre

