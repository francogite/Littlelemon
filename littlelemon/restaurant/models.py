from django.db import models

# Create your models here.
class Booking(models.Model):
    # id = models.SmallIntegerField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(max_length=6)
    bookingDate = models.DateTimeField(max_length=6)
    
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    # id = models.SmallIntegerField(max_length=5, primary_key=True)    
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(max_length=5)
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
