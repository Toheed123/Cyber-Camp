from django.db import models
from django.db.models.fields import CharField



class contact(models.Model):
    Name=models.CharField(max_length=200, null=True)
    Email=models.CharField(max_length=200, null=True)
    Message=models.CharField(max_length=200, null=True)
    Mobile_Number=models.IntegerField(default=0, null=True)
    
    # admin site display name
    def __str__(self):
        return f"{self.Name}, {self.Email}"