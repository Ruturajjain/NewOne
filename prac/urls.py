from django.urls import  include,path
from rest_framework import routers
from prac.views import StudentViewset,CollegeViewset

router = routers.DefaultRouter()
router.register(r'stud',StudentViewset)
router.register(r'colg',CollegeViewset)

