from django.contrib import admin
from quickstart.models.partmodels import part
from quickstart.models.contactmodels import contact


class partadmin(admin.ModelAdmin):
    list_display=['State_Code','AC_No','Part_No','SI_No_In_Part','EPIC_No','Name','Age','Gender','RLn_Name','RLN_Type']
    # fields = ['image_tag']
    # readonly_fields = ['image_tag']
class contactadmin(admin.ModelAdmin):
    list_display=['Name','Mobilr_Number','Email','Message']
@admin.register(part)
class partAdmin(admin.ModelAdmin):
    list_display=('id','Name','Age','Gender','SI_No_In_Part','Part_No','Epic_No','Mobile_Number','Image_Url','admin_photo')
    # readonly_fields = ('Name')

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display=('Name','Mobile_Number','Email','Message')
