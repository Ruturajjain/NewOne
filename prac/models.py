from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    name  = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    marks = models.IntegerField()
    is_deleted = models.BooleanField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'stud'
        
        
class College(models.Model):
    name  = models.CharField(max_length=100)
    staff_count = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'colg'
        
    
# class Subject(models.Model):
#     name  = models.CharField(max_length=100)
#     marks = models.IntegerField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
#     def __str__(self):
#         return self.name
    
#     class Meta:
#         db_table = 'subj'
        
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)