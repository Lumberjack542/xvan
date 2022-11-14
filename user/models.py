from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=120, unique=True)
    #REQUIRED_FIELDS = ['first name', 'last name']

    def __str__(self):
        return f"{self.username}"


class Category(models.Model):
    name_category = models.CharField(max_length=120)

    def __str__(self):
        return self.name_category
    # self_care = 'self care'
    # salary = 'salary'
    # health_and_fitness = 'health_and_fitness'
    # cafe = 'cafe'
    # education = 'education'
    # car = 'car'
    # relaxation = 'relaxation'
    # payments = 'Payments, commissions'
    # shopping = 'Shopping: clothes, appliances'
    # products = 'products'
    # travel = 'travel'
    # choice = [
    #     (self_care, "self_care"),
    #     (salary, "salary"),
    #     (health_and_fitness, "health_and_fitness"),
    #     (cafe, "cafe"),
    #     (relaxation, "relaxation"),
    #     (payments, "payments"),
    #     (shopping, "shopping"),
    #     (products, "products"),
    #     (travel, "travel")
    # ]


class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    cat = models.ManyToManyField(Category)
    balance = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user}"


class Transaction(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sum = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    organisation = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f'{self.user}'
