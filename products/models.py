from django.db import models

class Products (models.Model):
    image = models.ImageField('Изображение', upload_to= 'products_images')
    name = models.CharField('Название', max_length = 50)
    description = models.TextField('Описание')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'