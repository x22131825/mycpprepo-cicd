from django.db import models

# Create your models here.
class Parking(models.Model):
    # id = models.BigAutoField(primary_key=True)
        ownername=models.CharField(max_length=25,blank=False,null=True)
        contact=models.IntegerField()
        parkingslot=models.IntegerField()
        entrydatetime=models.DateTimeField()
        vehicle=models.CharField(max_length=25)

        def __str__(self) :
            return self.ownername