from rest_framework import serializers 
from .models import *

class librarySerializer(serializers.ModelSerializer):
    class Meta:
        model = librarymodel
        fields=['name','class_name','img','url']
