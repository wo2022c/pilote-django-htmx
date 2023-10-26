from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)    
    description = models.TextField()
    town = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    street = models.CharField(max_length=255, null=True)
    #photo = models.ImageField(upload_to='profile_pics', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = True

    def __str__(self):
        return self.user_name

class Pet(models.Model):
    name = models.CharField(max_length=255)
    date_birth = models.DateField()
    breed = models.CharField(max_length=255)
    vaccinated = models.BooleanField()
    sterilized = models.BooleanField()
    has_allergies = models.BooleanField()
    description = models.TextField()
    #photo = models.ImageField(upload_to='pet_pics', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)    
    #user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class PetOwner(UserProfile):
    pets = models.ManyToManyField(Pet)    

    def __str__(self):
        return self.user_name + " Pet owner "