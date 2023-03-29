from django.db import models

# Create your models here.

class Conference(models.Model):

    def __str__(self):
        return f'{self.titre}'

    titre = models.fields.CharField(max_length=50)
    description = models.fields.CharField(max_length=255)
    logo = models.ImageField(upload_to='preview_app/static/images', blank=True, null=True)

class Jour(models.Model):

    date = models.DateField(primary_key=True)



class Salle(models.Model):

    def __str__(self):
        return f'{self.titre}'

    titre = models.fields.CharField(max_length=50)
    # Date a corriger pour afficher que les jours
    date = models.fields.DateField()
    


class Session(models.Model):

    def __str__(self):
        return f'{self.titre}'

    titre = models.fields.CharField(max_length=50)
    # Date a corriger pour les horraires
    date = models.fields.DateField()
    id_salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

class Intervenant(models.Model):

    def __str__(self):
        return f'{self.nom, self.prenom}'

    nom = models.fields.CharField(max_length=50)
    prenom = models.fields.CharField(max_length=50)

    # Photo à voir si token ou autre manière à enregistrer
    logo = models.ImageField(upload_to='', blank=True, null=True)

class Presentation(models.Model):

    def __str__(self):
        return f'{self.titre}'

    titre = models.fields.CharField(max_length=50)
    description = models.fields.CharField(max_length=255)

    # Pptx a voir comment ça va être enregistré
    fichier_pptx = models.fields.CharField(max_length=60)
    id_session = models.ForeignKey(Session, on_delete=models.CASCADE)

# A demander comment faire la table croisée

class InterPresent(models.Model):

    def __str__(self):
        return f'{self.id_presentation}'

    id_presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    id_intervenant = models.ForeignKey(Intervenant,null= True, on_delete=models.SET_NULL)