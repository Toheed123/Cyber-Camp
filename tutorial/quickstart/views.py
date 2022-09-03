from django.shortcuts import render
from django.contrib.auth.models import User, Group
import django_filters
from django_filters.rest_framework.backends import DjangoFilterBackend
# from quickstart.models import part
from rest_framework import viewsets
from rest_framework import permissions
#from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from quickstart.serializers import UserSerializer, GroupSerializer
from quickstart.serializers import partSerializer
from quickstart.serializers import contactSerializer
#from tutorial.quickstart.models import part
from quickstart.models.partmodels import part
from quickstart.models.contactmodels import contact
from rest_framework import generics
#from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import quickstart_views  
#from django_filters.rest_framework import DjangoFilterBackend
from django.core.validators import MaxValueValidator, MinValueValidator






class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.
class partViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = part.objects.all().order_by('id')
    # 
    # queryset = part.objects.filter(Name__icontains='my_substring')
    
    serializer_class = partSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    
    # filterset_fields = ['Name','Gender','Mobile_Number','AC_No','Epic_No','Age','Part_No','SI_No_In_Part','RLn_Name','RLN_Type','id']
    # u = django_filters.rest_framework.CharFilter(name='Name', lookup_expr='exact')
    # u__contains = django_filters.rest_framework.CharFilter(name='Name', lookup_expr='contains')
    filterset_fields = {
    
        'Name': ['icontains'],
        'Gender': ['exact'],
        'Mobile_Number': ['icontains'],
        'AC_No': ['icontains'],
        'Epic_No': ['icontains'],
        'Part_No': ['icontains'],
        'SI_No_In_Part': ['icontains'],
        'RLn_Name': ['icontains'],
        'RLN_Type': ['icontains'],
        'id': ['exact'],
        'Age':['exact']


    }
    part.objects.order_by('SI_No_In_Part')
    part.objects.filter(Name='Name')
    # queryset = queryset.filter(username__istartswith='Name')
class contactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = contact.objects.all()
    serializer_class = contactSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['Age', 'Epic_No']
# @quickstart_views(["POST"])

@csrf_exempt
def login(request):

    print(request.POST)
    if (request.method=="POST"):
        a = request.POST['username']
        b = request.POST['password']
        user = authenticate(username=a, password=b)
        if user is not None:
        # A backend authenticated the credentials
            return JsonResponse({'success':True})
        else:
        # No backend authenticated the credentials
            return JsonResponse({'success':False})
    else:
        return JsonResponse({'success':False})


# class models(part):
#     limited_integer_field = Mobile_Number(
        
#         validators=[
#             MaxValueValidator(9),
#             MinValueValidator(6)
#         ]
#      )