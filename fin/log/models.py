from django.db import models

# Create your models here.
class User2(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    number=models.CharField(max_length=20)
    position=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=400)
    def _unicode_(self):
        return self.username

class Ship(models.Model):
    #ShipSpeed=models.CharField(max_length=50)
    #Heading=models.CharField(max_length=20)
    #WindSpeed=models.CharField(max_length=20)
    dtmGPS=models.DateTimeField(auto_now_add=True)
    floLON=models.CharField(max_length=50)
    vchLonUnit=models.CharField(max_length=10)
    floLAT=models.CharField(max_length=50)
    vchLatUnit=models.CharField(max_length=10)
    floSPD=models.CharField(max_length=50)
    floDIR=models.CharField(max_length=50)
    floHDT=models.CharField(max_length=50)
    floHDM=models.CharField(max_length=50)
    floWST=models.CharField(max_length=50)
    floWSR=models.CharField(max_length=50)
    floWDT=models.CharField(max_length=50)
    floWDR=models.CharField(max_length=50)
    vchWdtUnit=models.CharField(max_length=10)
    floDPT=models.CharField(max_length=50)
    floVLW=models.CharField(max_length=50)
    def _unicode_(self):
        return self.dtmGPS
    class Meta:
        ordering=['-dtmGPS']
    
