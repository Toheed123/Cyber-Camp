
from django.db import models
from django.db.models.fields import CharField
from django.utils.html import escape
from django.utils.safestring import mark_safe
# from django.core.validators import MaxValueValidator, MinValueValidator


class part(models.Model):
    State_Code = models.CharField(max_length=200, null=True)
    AC_No = models.IntegerField(default=0, null=True)
    Part_No = models.IntegerField(default=0, null=True)
    SI_No_In_Part = models.IntegerField(default=0, null=True)
    Epic_No = models.CharField(max_length=200, null=True)
    Name = models.CharField(max_length=200, null=True)
    Age = models.IntegerField(default=0, null=True)
    Gender = models.CharField(max_length=200, null=True)
    RLn_Name = models.CharField(max_length=200, null=True)
    RLN_Type = models.CharField(max_length=200, null=True)
    Mobile_Number = models.BigIntegerField(default=0, null=True)
    Image_Url = models.ImageField(upload_to='image',max_length=200,null=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.Image_Url.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
    # def __str__(self):
        # return self.Name







    