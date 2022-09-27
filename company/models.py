from django.urls import reverse
from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='media/company')
    description = models.CharField(max_length=300, null=False)
    color = models.CharField(max_length=30, null=True)

    def imageURL(self):
        try:
            image_url = self.image.url
        except:
            image_url = ''
        return image_url

    def __str__(self) -> str:
        return self.name
