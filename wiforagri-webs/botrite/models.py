# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
#from django.contrib.postgres.fields import ArrayField

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])



class Daily(models.Model):
    hod = models.FloatField(default=1)# ,blank=False, null=False) 
    temperature = models.FloatField(default=0)#,blank=False, null=False) 
    humidity = models.FloatField(default=10)#,blank=False, null=False) 
    leafwetness = models.FloatField(default=0)#,blank=False, null=False) 
    rain = models.FloatField(default=0)#,blank=False, null=False) 
    GS = models.FloatField(default=0)#,blank=False, null=False) 
    treatment=models.BooleanField(default=False)#,blank=False, null=False)    
            

class State(models.Model):
    LotId =  models.TextField(default='000000')
    year= models.FloatField(default=2000) #models.IntegerField()
    doy = models.FloatField(default=1) #models.IntegerField()
    cumulateInfection = models.FloatField(default=0) #models.IntegerField()
    cumulateInfectionBerry = models.FloatField(default=0) #models.IntegerField()
    
        
class Data(models.Model):
    daily=models.ForeignKey(to=Daily, on_delete=models.CASCADE)
    LotId =  models.TextField(default='000000')
    year= models.FloatField(default=2000) #models.IntegerField()
    doy = models.FloatField(default=1) #models.IntegerField()

    
    
class Botrite(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    state=models.ForeignKey(to=State, on_delete=models.CASCADE)
    data=models.ForeignKey(to=Data, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created']
        #managed = False