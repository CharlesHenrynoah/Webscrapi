from django.db import models

#Création du model de task de scrapping unitaire 
class ScrappingTask(models.Model): # Hérite de la classe Model De Django
    #Pour L"Url à scrapper 
    url = models.URLField(max_length=500) #Champ de type Urlfield de taille max 500 caractères

    #Date et heure de création de la tache 
    created_at = models.DateTimeField(auto_now_add=True) #Ce champ est automatiquement rempli à la création de l'objet

    #Date et heure de mise à jour de la tache 
    updated_at = models.DateTimeField(auto_now=True) #Ce champ est automatiquement rempli à chaque mise à jour de l'objet

    #Etat de la tache 
    STATUS_CHOICES = [
        ('PENDING','Pending'), #En attente
        ('RUNNING','Running'), #En cours d'execution
        ('COMPLETED','Completed'), #Terminé
        ('ERROR','Error'), #Erreur
    ]
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='PENDING') #Ceci est l'etat par defaut 

    #Pour les sélecteurs à utiliser
    selectors = models.TextField(help_text="Entrez les sélecteurs au format JSON.") #Champ de type Textfield

    #Conversion de l'objet en chaine de caractère
    def __str__(self):
        return self.url 
    
class ScrapedData(models.Model):
    # Lien vers la tache de scrapping associée 
    task = models.ForeignKey(ScrappingTask,on_delete=models.CASCADE) #Lorsque la tache est supprimée, les données associées sont supprimées

    #Contenu extrait 
    title = models.CharField(max_length=500) #Champ de type Charfield de taille max 500 caractères
    paragraph = models.TextField() #Champ de type Textfield
    date = models.DateField() #Champ de type Datefield

    #Conversion de l'objet en chaine de caractère
    def __str__(self):
        return f"Data from {self.task.url}"


