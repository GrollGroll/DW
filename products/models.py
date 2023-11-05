from django.db import models

class Products (models.Model):
    # Image = models.ImageField
    Name = models.CharField('name', max_length = 50)
    Description = models.TextField('description')
    Price = models.IntegerField('price')

def __str__(self):
    return self.Name
