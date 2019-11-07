from django.db import models
from django.utils import timezone

class Supervisor(models.Model):
    picture = models.ImageField(upload_to='image')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=90)
    telephone = models.CharField(max_length=80)
    speciality = models.CharField(max_length=80)
    departements = models.CharField(max_length=70,null=True, blank=True)
    #first supervisor considered as coordinator
    post = models.CharField(max_length=50, blank=True)



    def __str__(self):
        return self.name


class Project(models.Model):
    image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=3000)
    technology = models.CharField(max_length=100)
    supervisor = models.ForeignKey(Supervisor, related_name= 'projects', on_delete=models.SET_NULL, null=True)
    link = models.URLField(max_length=120,blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Student(models.Model):
    photo = models.ImageField(upload_to='image')
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=70)
    technologies = models.CharField(max_length=100)
    telephone = models.CharField(max_length=70)
    reg_numb = models.IntegerField()
    biography = models.TextField(max_length=1000)
    project = models.ForeignKey(Project, related_name='students', on_delete=models.CASCADE)


    def __str__(self):
        return self.name




class Contact_us(models.Model):
    firstname = models.CharField(max_length=20)
    lastname =  models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    message = models.TextField(max_length=10000)

    def __str__(self):
        return self.firstname

