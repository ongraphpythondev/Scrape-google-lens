from django.db import models


# Create your models here.

class Save_img(models.Model):
    upload = models.ImageField(upload_to='uploads/')

    # def __str__(self):
    #     return str(self.upload)
