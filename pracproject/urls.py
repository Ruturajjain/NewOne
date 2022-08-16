"""pracproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from prac.views import *
from django.contrib import admin
from django.urls import path, include, re_path
from prac.urls import router
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import obtain_auth_token
schema_view = get_swagger_view(title='Studetn Operation API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('login/', obtain_auth_token, name='login'),
    # re_path(r'^$', schema_view),
    
    #Concrete APIView classess
    path("s-list-c/", StudListC.as_view()),      
    path("s-create-c/", StudCreateC.as_view()),      
    path("s-retr-c/<int:pk>/", StudRetrC.as_view()),      
    path("s-updt-c/<int:pk>/", StudUpdtC.as_view()),      
    path("s-detr-c/<int:pk>/", StudDetrC.as_view()),
]
