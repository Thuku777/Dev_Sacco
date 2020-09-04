from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Feature(models.Model):
    select_service = models.ForeignKey(Service, on_delete=models.SET_NULL, related_name='feature_services', blank=True, null=True)
    service_feature = models.CharField(max_length=255)
    
    def __str__(self):
        return self.service_feature
