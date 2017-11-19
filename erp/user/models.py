from django.db import models


class Company(models.Model):
    RELATIONSHIP = (
        ('C', 'Client'),
        ('P', 'Proveedor')
    )

    name = models.CharField(max_length=150)
    rut = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    area = models.CharField(max_length=500)
    relationship = models.CharField(max_length=1, choices=RELATIONSHIP)


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)


class Worker(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=50)
    man_hour = models.FloatField()

