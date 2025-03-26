from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://cdn.vectorstock.com/i/500p/42/11/creative-concept-of-brain-food-symbolized-vector-53434211.jpg")

    def __str__(self):
        return self.item_name
    