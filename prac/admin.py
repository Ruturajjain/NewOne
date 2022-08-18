from django.contrib import admin

from prac.models import College, Student, Subject

# Register your models here.

admin.site.register([Student,College,Subject])