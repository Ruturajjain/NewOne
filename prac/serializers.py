from prac.models import *
from rest_framework import serializers



class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class Collegeserializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

# class Subjectserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = '__all__'       