from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    author = models.CharField(max_length=50,null=True,blank=True)
    year = models.IntegerField(max_length=5,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['name','author','year']
 
    def __str__(self):
           return self.name
