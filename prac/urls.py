from django.urls import  include,path
from rest_framework import routers
from prac.views import *

router = routers.DefaultRouter()
router.register(r'stud',StudentViewset)
router.register(r'colg',CollegeViewset)
router.register(r'subj',SubjectViewset)


