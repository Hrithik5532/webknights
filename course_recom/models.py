
from django.db import models



# Create your models here.
class librarymodel(models.Model):
    name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=10,default=None,null=True)
    img= models.URLField()
    url = models.URLField()
    def __str__(self):
       return self.name + '-' + self.class_name 
   