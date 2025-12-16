from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=244)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/static', width_field='image_width', height_field='image_height')
    image_width = models.IntegerField(blank=True)
    image_height = models.IntegerField(blank=True)
    SIZE_CHOICE = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
        ('GG', 'Extra Grande')
    )
    size = models.CharField(max_length=2, choices=SIZE_CHOICE, default='P')