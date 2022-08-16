from django.contrib import admin

from prac.models import College, Student

# Register your models here.

admin.site.register([Student,College])