from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    job=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Peoples(models.Model):
    job_choices=[
        ('EMPLOYEE','employee'),
        ('MANAGER','manager')
    ]
    user_id=models.CharField(max_length=50,unique=True,null=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    role=models.CharField(max_length=10,choices=job_choices,default='EMPLOYEE')

    def __str__(self):
        return self.name
    