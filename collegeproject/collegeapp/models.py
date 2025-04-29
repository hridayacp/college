from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    usertype=models.CharField(max_length=50)


class Department(models.Model):
    Dep_Name=models.CharField(max_length=100)

class Teacher(models.Model):
    dep_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    teach_id=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.BigIntegerField()
    Qualification=models.CharField(max_length=100)

class student(models.Model):
    dep_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    stud_id=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=100)

class Staff(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='staff_photo/')


# Create your models here.
