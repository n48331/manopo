from django.db import models

# Create your models here.

class search(models.Model):
    name = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'pics')

    def __str__(self):
        return self.name+' || '+ self.house

class document(models.Model):
    name = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    doctype =  models.CharField(max_length=255)
    docno = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pics/docs/")



    def __str__(self):
        return self.name +' || '+ self.house+' || '+ self.doctype