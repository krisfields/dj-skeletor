from model_mommy.recipe import Recipe
from .models import User
from faker import Factory

fake = Factory.create()

user = Recipe(
    User,
    first_name=fake.first_name,
    last_name=fake.last_name,
    email=fake.email,
    username=fake.user_name,
    about=fake.paragraph
)
