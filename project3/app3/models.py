from django.db import models


class foodcart(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length = 150)
    price = models.IntegerField()

