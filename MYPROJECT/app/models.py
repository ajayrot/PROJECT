from django.db import models

class State(models.Model):
    idno = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50)

class City(models.Model):
    idno = models.CharField(max_length=20,primary_key=True)
    state_name = models.ForeignKey(State,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

class UserRegister(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    city_name = models.ForeignKey(City,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100,primary_key=True)
    password = models.CharField(max_length=50)


class BuyUsedcars(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to="hero_headshots/")

class SellUsedcars(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to="hero_headshots/")

class Newcars(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to="hero_headshots/")


