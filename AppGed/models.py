from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_categorie

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

class Groupe(models.Model):
    nom_groupe = models.CharField(max_length=10)

    def __str__(self):
        return self.nom_groupe

    class Meta:
        verbose_name = "Groupe"
        verbose_name_plural = "Groupes"

class Document(models.Model):

    nom_document = models.CharField(max_length=50, verbose_name='Nom du Document')
    piecejointe = models.FileField(upload_to='public', verbose_name='Fichier')
    remarque = models.TextField(max_length=512)
    categorie = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING, verbose_name='Catégorie')
    groupe = models.ForeignKey(Groupe, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nom_document


    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
