from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from tkinter import CASCADE
from finalback.common import get_upload_path
# Create your models here.




class role(models.Model):



    
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    roles = models.CharField(max_length=200, null=True)


    class Meta:
        ordering = ['created']

class Weights(models.Model):

 
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    masse_en_killograme = models.IntegerField()
    min=models.IntegerField(null=True,blank=True)
    max=models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return  str(self.masse_en_killograme)


class Categorie(models.Model):

 
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    categorie_age = models.CharField(max_length=200,null=True, blank=True)
    min=models.IntegerField(null=True,blank=True)
    max=models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return  self.categorie_age


class Grade(models.Model):

 
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    Grade = models.CharField(max_length=200,null=True, blank=True)

    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return  self.Grade
        
        
class Degree(models.Model):
    
 
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    Degree = models.CharField(max_length=200,null=True, blank=True)

    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return  self.Degree

class Seasons(models.Model):

 
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    Seasons = models.CharField(max_length=200, null=True, blank=True)
    activated =models.BooleanField(default=False)
    
    
    def __str__(self):
        return  self.Seasons


    class Meta:
        ordering = ['created']
        


class Licences(models.Model):


    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    role =models.ForeignKey(role, null=True, blank=True, on_delete=models.DO_NOTHING)
    seasons =models.ForeignKey(Seasons, null=True, blank=True, on_delete=models.DO_NOTHING)
    created = models.DateField(auto_now_add=True)
    num_licences = models.TextField(primary_key=True,)
    
    activated =models.BooleanField(default=False)
    state=models.TextField(default="En Attente")
    verified =models.BooleanField(default=False)
    degree =models.ForeignKey(Degree, null=True, blank=True, on_delete=models.DO_NOTHING)
    grade =models.ForeignKey(Grade, null=True, blank=True, on_delete=models.DO_NOTHING)
    weight =models.ForeignKey(Weights, null=True, blank=True, on_delete=models.DO_NOTHING)
    categorie =models.ForeignKey(Categorie, null=True, blank=True, on_delete=models.DO_NOTHING)
    club =models.ForeignKey('finalback.Club', null=True, blank=True, on_delete=models.DO_NOTHING)
    discipline =models.ForeignKey('finalback.Discipline', null=True, blank=True, on_delete=models.DO_NOTHING)




class ArchivedLicences(models.Model):
    

    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    role =models.ForeignKey(role, null=True, blank=True, on_delete=models.DO_NOTHING)
    seasons =models.ForeignKey(Seasons, null=True, blank=True, on_delete=models.DO_NOTHING)
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    num_licences = models.TextField( blank=True)
    
    activated =models.BooleanField(default=False)
    state=models.TextField(default="En Attente")
    verified =models.BooleanField(default=False)
    degree =models.ForeignKey(Degree, null=True, blank=True, on_delete=models.DO_NOTHING)
    grade =models.ForeignKey(Grade, null=True, blank=True, on_delete=models.DO_NOTHING)
    weight =models.ForeignKey(Weights, null=True, blank=True, on_delete=models.DO_NOTHING)
    categorie =models.ForeignKey(Categorie, null=True, blank=True, on_delete=models.DO_NOTHING)
    club =models.ForeignKey('finalback.Club', null=True, blank=True, on_delete=models.DO_NOTHING)
    discipline =models.ForeignKey('finalback.Discipline', null=True, blank=True, on_delete=models.DO_NOTHING)



    class Meta:
        ordering = ['created']



class Profile(models.Model):
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    

    sexe=models.TextField(null=True,blank=True)
    role =models.ForeignKey(role, null=True, blank=True, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # categorie = models.ForeignKey(Categorie, null=True, on_delete=models.DO_NOTHING)
    licences = models.ForeignKey(Licences, null=True, on_delete=models.CASCADE)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    profile_photo = models.TextField(  null=True, blank=True)
    phone = models.IntegerField(null=True,blank=True)
    location = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    cin = models.TextField(null=True, blank=True)
    

    class Meta:
        ordering = ['created']



    
        
class Club(models.Model):
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    ligue =models.ForeignKey('finalback.Ligue', null=True, blank=True, on_delete=models.DO_NOTHING)
    logo =models.TextField(null=True,blank=True)
    

    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return  self.name


class Supporter(models.Model):
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    club = models.OneToOneField(Club, null=True,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    club = models.ForeignKey(Club,null=True, blank=True, on_delete=models.DO_NOTHING) 
    
    class Meta:
        ordering = ['created']



class Arbitrator(models.Model):
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    identity_photo = models.TextField(null=True,blank=True)
    grade=models.ForeignKey(Grade, on_delete=models.DO_NOTHING,null=True,blank=True)
    photo = models.TextField(null=True,blank=True)
    club = models.ForeignKey(Club,null=True, blank=True, on_delete=models.DO_NOTHING)   

    class Meta:
        ordering = ['created']

class Coach(models.Model):
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.DO_NOTHING)
    degree=models.ForeignKey(Degree, null=True, on_delete=models.DO_NOTHING)
    identity_photo = models.TextField(null=True,blank=True)
    degree_photo = models.TextField(null=True,blank=True)
    grade_photo = models.TextField(null=True,blank=True)
    photo=models.TextField(null=True,blank=True)
    club = models.ForeignKey(Club,null=True, blank=True, on_delete=models.DO_NOTHING)
    category_id=models.ForeignKey(Categorie,null=True, on_delete=models.DO_NOTHING)
    weights=models.ForeignKey(Weights,null=True, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['created']

class Athlete(models.Model):
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    #first_name = models.TextField(null=True, blank=True)
    # last_name = models.TextField(null=True, blank=True)
    # sex = models.TextField(null=True, blank=True)
    category_id = models.IntegerField(null=True, blank=True)
    grade_id = models.IntegerField(null=True, blank=True)
    # birthday = models.DateField(null=True, blank=True)
    id_degree = models.IntegerField(null=True, blank=True)
    # nationality =models.TextField(null=True, blank=True)
    photo = models.TextField( null=True, blank=True)
    identity_photo = models.TextField(  null=True, blank=True)
    medical_photo = models.TextField(  null=True, blank=True)
    discipline=models.ForeignKey('finalback.Discipline', on_delete=models.DO_NOTHING)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)
    weights = models.ForeignKey(Weights, null=True, on_delete=models.DO_NOTHING)
    club = models.ForeignKey(Club,null=True, blank=True, on_delete=models.DO_NOTHING)
    


    class Meta:
        ordering = ['created']
        
        
        
        
class Ligue(models.Model):
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    
    

    class Meta:
        ordering = ['created']
        
        
class Discipline(models.Model):
    created = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    image=models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    

    class Meta:
        ordering = ['created']
        
class Competition(models.Model):
    id=models.AutoField(primary_key=True)
    created = models.DateField(auto_now_add=True)
    name = models.TextField(null=True, blank=True)
    manager= models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    duration=models.IntegerField(null=True,blank=True)
    date=models.DateField(null=True, blank=True),
    max_participants=models.IntegerField(null=True, blank=True)
    max_attendents=models.IntegerField(null=True, blank=True)
    attendents=models.IntegerField(null=True, blank=True)
    country=models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    location=models.TextField(null=True,blank=True)
    status=models.TextField(default="En Attante")
    participants=models.ManyToManyField(Athlete, null=True,blank=True)
    arbitrators=models.ManyToManyField(Arbitrator, null=True,blank=True)
    age=models.ForeignKey(Categorie, on_delete=models.DO_NOTHING,null=True, blank=True)
    season=models.ForeignKey(Seasons, on_delete=models.DO_NOTHING,null=True, blank=True)
    ligue=models.ForeignKey(Ligue, on_delete=models.DO_NOTHING,null=True, blank=True)
    discipline=models.ForeignKey(Discipline, on_delete=models.DO_NOTHING,null=True, blank=True)
    
    
class Bracket(models.Model):
    id=models.AutoField(primary_key=True)
    stage=models.TextField(null=True,blank=True)
    created = models.DateField(auto_now_add=True)

    
class Match(models.Model):
    id=models.AutoField(primary_key=True)
    created = models.DateField(auto_now_add=True)
    participant1=models.ForeignKey(Athlete, on_delete=models.DO_NOTHING,related_name='participant1',null=True,blank=True)
    participant2=models.ForeignKey(Athlete, on_delete=models.DO_NOTHING,related_name='participant2',null=True,blank=True)
    is_final=models.BooleanField(default=False,null=True,blank=True)
    arbitrator=models.ForeignKey(Arbitrator, on_delete=models.DO_NOTHING,null=True,blank=True)
    datetime=models.DateField(null=True,blank=True)
    bracket=models.ForeignKey(Bracket, on_delete=models.DO_NOTHING,null=True,blank=True)
    result=models.ForeignKey('finalback.Result', on_delete=models.DO_NOTHING,null=True,blank=True)
    status=models.TextField(default="En Attente",null=True,blank=True)
    comp=models.ForeignKey(Competition, on_delete=models.DO_NOTHING,null=True,blank=True)
    
    
class Result(models.Model):
    winner=models.ForeignKey(Athlete, on_delete=models.DO_NOTHING,null=True,blank=True)
    p1_points=models.IntegerField(null=True,blank=True)
    p2_points=models.IntegerField(null=True,blank=True)
    duration=models.FloatField(null=True,blank=True)
    notes=models.TextField(null=True,blank=True)


class Image(models.Model):
    url=models.ImageField(upload_to=get_upload_path)
    path=models.TextField(null=False,blank=False)
    size=models.FloatField(null=True,blank=True)
    name=models.TextField(null=True,blank=True)
    extension=models.TextField(null=True,blank=True)
    type=models.TextField(null=True,blank=True)
    uploaded=models.DateField(auto_now_add=True)
    season=models.ForeignKey(Seasons, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Username(models.Model):
    created_username=models.TextField(null=False,blank=False,max_length=10,unique=True,default=1000000000)
    created = models.DateField(auto_now_add=True)
   

    
    

