from django.shortcuts import render
from rest_framework.viewsets import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from prac.models import College, Student, Subject
from prac.serializers import Collegeserializer, Studentserializer, Subjectserializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
# Create your views here.

class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    
class CollegeViewset(ModelViewSet):
    queryset = College.objects.all()
    serializer_class = Collegeserializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class SubjectViewset(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = Subjectserializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

class StudListC(ListAPIView):      #inherit genericApiview, ListModelMixin
    queryset = Student.objects.all()    #genericApi
    serializer_class = Studentserializer  #genericApi
    
class StudCreateC(CreateAPIView):
    queryset = Student.objects.all()    #genericApi
    serializer_class = Studentserializer  #genericApi
    
class StudRetrC(RetrieveAPIView):
    queryset = Student.objects.all()    #genericApi
    serializer_class = Studentserializer  #genericApi
    
class StudUpdtC(UpdateAPIView):
    queryset = Student.objects.all()    #genericApi
    serializer_class = Studentserializer  #genericApi
    
class StudDetrC(DestroyAPIView):
    queryset = Student.objects.all()    #genericApi
    serializer_class = Studentserializer  #genericApi