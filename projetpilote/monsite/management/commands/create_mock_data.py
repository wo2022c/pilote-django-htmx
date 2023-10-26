from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
#from your_app_name.models import Dog, DogOwner, DogSitter, Booking, Review
# Import necessary models and User model
from django.contrib.auth.models import User

import os
import django
import random
from datetime import datetime, timedelta

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monsite.settings')  # Replace 'your_project_name' with your actual project name
# django.setup()

from django.contrib.auth.models import User
from monsite.models import UserProfile, Pet, PetOwner  # Replace 'your_app_name' with your actual app name
# from faker import Faker
# fake = Faker()

# def create_users(n=10):
#     for _ in range(n):
#         username = fake.user_name()
#         email = fake.email()
#         password = User.objects.make_random_password()
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.first_name = fake.first_name()
#         user.last_name = fake.last_name()
#         user.save()
#         yield user

# def create_user_profiles(users):
#     for user in users:
#         profile = UserProfile.objects.create(
#             user=user,
#             user_name=fake.user_name(),
#             phone=fake.phone_number(),
#             description=fake.text(),
#             town=fake.city(),
#             zip_code=fake.zipcode(),
#             street=fake.street_name(),
#             # Assuming you've set up media files properly, you can add fake images
#             # photo=...  
#         )
#         yield profile

# def create_pets(n=10):
#     for _ in range(n):
#         pet = Pet.objects.create(
#             name=fake.first_name(),
#             date_birth=fake.date_this_century(),
#             breed=fake.word(),
#             vaccinated=fake.boolean(),
#             sterilized=fake.boolean(),
#             has_allergies=fake.boolean(),
#             description=fake.text(),
#             # photo=...
#         )
#         yield pet

# def create_pet_owners(profiles, pets):
#     for profile in profiles:
#         owner = PetOwner.objects.create(userprofile_ptr_id=profile.pk)
#         owner.pets.set(random.sample(list(pets), k=random.randint(1, 3)))  # assigning 1-3 random pets to an owner
#         yield owner

# def create_pet_sitters(profiles):
#     for profile in profiles:
#         sitter = PetSitter.objects.create(
#             userprofile_ptr_id=profile.pk,
#             capacity=random.randint(1, 5)
#         )
#         yield sitter

# def create_bookings(owners, sitters, chats):
#     for i, owner in enumerate(owners):
#         booking = Booking.objects.create(
#             pet=random.choice(owner.pets.all()),
#             pet_owner=owner,
#             pet_sitter=random.choice(sitters),
#             start_date=fake.date_this_year(),
#             end_date=fake.date_this_year(),
#             status=random.choice([choice[0] for choice in Booking.STATUS_CHOICES]),
#             chat=chats[i]
#         )
#         yield booking

# def create_chats(n=10):
#     for _ in range(n):
#         chat = Chat.objects.create()
#         yield chat

# def create_messages(chats, users, n=5):
#     for chat in chats:
#         for _ in range(n):
#             Message.objects.create(
#                 chat=chat,
#                 user=random.choice(users),
#                 content=fake.sentence()
#             )

# def create_reviews(owners, sitters):
#     for sitter in sitters:
#         Review.objects.create(
#             pet_sitter=sitter,
#             pet_owner=random.choice(owners),
#             rating=random.randint(1, 5),
#             comment=fake.text()
#         )

# def generate_mock_data():
#     users = list(create_users())
#     profiles = list(create_user_profiles(users))
#     pets = list(create_pets())
#     owners = list(create_pet_owners(profiles[:5], pets))  # using first 5 profiles for pet owners
#     sitters = list(create_pet_sitters(profiles[5:]))  # using last 5 profiles for pet sitters
#     chats = list(create_chats())
#     bookings = list(create_bookings(owners, sitters, chats))
#     create_messages(chats, users)
#     create_reviews(owners, sitters)

class Command(BaseCommand):
    help = 'Create mock data for the app'

    # def handle(self, *args, **kwargs):
    #     # [Paste the Python code I provided here]
    #     self.stdout.write(self.style.SUCCESS('Successfully created mock data'))
    def handle(self, *args, **kwargs):
        #generate_mock_data()
        # Create two users for petowners
        # Create two pet owners                    
        # Create two pets for each owner
        # Create two users for pet sitters
        # Create two pet sitters
        # Create 10 bookings with reviews
        # Create two users for pet owners
        # 1. Create two users for pet owners

        # 1. Create two users for pet owners
        user_owner_1 = User.objects.create(username='owner1', password='owner1password')
        user_owner_2 = User.objects.create(username='owner2', password='owner2password')

        # 2. Create two pet owners
        pet_owner_1 = PetOwner.objects.create(user=user_owner_1, user_name='owner1_username', phone='123456789', description='owner1_description', town='Town1', zip_code='12345', street='Street1')
        pet_owner_2 = PetOwner.objects.create(user=user_owner_2, user_name='owner2_username', phone='987654321', description='owner2_description', town='Town2', zip_code='67890', street='Street2')

        # 3. Create two pets for each owner
        pet1_owner1 = Pet.objects.create(name='Buddy', date_birth='2020-01-01', breed='Bulldog', vaccinated=True, sterilized=True, has_allergies=False, description='A friendly dog')
        pet2_owner1 = Pet.objects.create(name='Rusty', date_birth='2021-01-01', breed='Poodle', vaccinated=True, sterilized=False, has_allergies=True, description='A playful dog')

        pet1_owner2 = Pet.objects.create(name='Snowy', date_birth='2019-01-01', breed='Husky', vaccinated=False, sterilized=True, has_allergies=False, description='A beautiful dog')
        pet2_owner2 = Pet.objects.create(name='Max', date_birth='2022-01-01', breed='Labrador', vaccinated=True, sterilized=True, has_allergies=False, description='A loyal dog')

        pet_owner_1.pets.add(pet1_owner1, pet2_owner1)
        pet_owner_2.pets.add(pet1_owner2, pet2_owner2)

        self.stdout.write(self.style.SUCCESS('Successfully created mock data'))