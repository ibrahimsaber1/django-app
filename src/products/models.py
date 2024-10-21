from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description =models.TextField(null=True, blank=True)
    price =models.DecimalField(decimal_places=2 , max_digits=12000)
    color = models.CharField(max_length=50)
    sammary = models.TextField(default="this ths a cool product")
    featured = models.BooleanField(default=True) 
    
    