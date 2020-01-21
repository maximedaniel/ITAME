from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class InteractiveSystem(models.Model):
    name = models.CharField(max_length=50)
    reference =  models.CharField(max_length=500)
    abstract =  models.CharField(max_length=500)

    def __unicode__(self):
    	return self.name

# Create your models here.
class Characteristic(models.Model):
    name = models.CharField(max_length=50)
    description =  models.CharField(max_length=500)
    interactive_systems = models.ManyToManyField(InteractiveSystem, blank=True)

    def __unicode__(self):
    	return self.name

# Create your models here.
class Criterium(models.Model):
    name = models.CharField(max_length=50)
    description =  models.CharField(max_length=500)
    characteristics = models.ManyToManyField(Characteristic, blank=True)

    def __unicode__(self):
    	return self.name

# Create your models here.
class Entity(models.Model):
    name = models.CharField(max_length=50)
    description =  models.CharField(max_length=500)
    criteria = models.ManyToManyField(Criterium, blank=True)

    def __unicode__(self):
    	return self.name