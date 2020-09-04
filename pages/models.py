from django.db import models

# Create your models here.
class About(models.Model):
    quote = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    about_photo = models.ImageField(upload_to='about_photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title
