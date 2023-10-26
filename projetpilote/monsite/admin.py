from django.contrib import admin

# Register your models here.

from .models import UserProfile, Pet, PetOwner

admin.site.register(UserProfile)
admin.site.register(Pet)
admin.site.register(PetOwner)
