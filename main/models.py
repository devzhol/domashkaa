from django.db import models

class Kiosk(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    kiosk = models.ForeignKey(Kiosk, on_delete=models.CASCADE, related_name='icecreams')

    def __str__(self):
        return self.name
class Parent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name