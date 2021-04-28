from django.db import models

# Create your models here.
class Produit(models.Model):
    name = models.CharField(max_length=50)
    libelle = models.CharField(max_length=45)
    prix = models.IntegerField()
    dateprod = models.DateField(auto_now_add=False, auto_now=False,null=True)

    
    class Meta:
        db_table = 'produits'
    def __str__(self):
        return "Prod : {}, lib: {}".format(self.name,self.libelle)

class Grade(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'grades'
    def __str__(self):
        return self.name
class Unite(models.Model):
    lib_unt = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'unites'
    def __str__(self):
        return self.lib_unt
class Personne(models.Model):
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE, null=True)
    qte = models.IntegerField(null=True)
    annee=models.IntegerField(null=True)
    
    class Meta:
        db_table = 'personnes'
    def __str__(self):
        return self.nom
class Etudient(models.Model):
    name = models.CharField(max_length=45)
    date_entr = models.DateField(auto_now_add=False, auto_now=False)
    photo=models.FileField(upload_to='photos/',null=True)
    
    class Meta:
        db_table = 'etudients'
        
    
    def __str__(self):
        return self.name


class Article(models.Model):
    libelle = models.CharField(max_length=40)
    class Meta:
        db_table = 'articles'
    def __str__(self):
        return self.libelle

class Facture(models.Model):
    reference = models.CharField(max_length=40)
    date_fact=models.DateField(auto_now_add=False,auto_now=False,null=True)
    class Meta:
        db_table = 'factures'
        
    def __str__(self):
        return self.reference


class Operation(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    qte = models.IntegerField()
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)

    class Meta:
        db_table = 'operations'
        unique_together = ("facture", "article")

    def __str__(self):
        return self.qte
