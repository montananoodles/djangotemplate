from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=100)
    views = models.IntegerField()
    cat = models.CharField(max_length=10)

    def __str__(self):
        return self.title
