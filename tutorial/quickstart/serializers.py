from django.contrib.auth.models import User, Group
from quickstart.models.partmodels import part
from quickstart.models.contactmodels import contact
from rest_framework import serializers

# from quickstart.models.loginmodels import login

#from tutorial.quickstart.models import part


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class partSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = part
        fields = ['State_Code','AC_No','Part_No','SI_No_In_Part','Epic_No','Name','Age','Gender','RLn_Name','RLN_Type','Mobile_Number','id','Image_Url']
        


class contactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = contact
        fields = ['Name','Email','Mobile_Number','Message']