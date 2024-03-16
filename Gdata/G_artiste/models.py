from django.db import models

# Create your models here.

class Artiste(models.Model):
   nom=models.CharField(max_length=255)
   prenom=models.CharField(max_length=255)
   categorie=models.CharField(max_length=255)
   biographie=models.TextField()
   
   def __str__(self):            
       return f"{self.nom}  {self.prenom}"
   
   