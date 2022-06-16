from django.db import models


# Create your models here.

def upload_path(instance, filename):
    return '/'.join(['media', str(instance.name), filename])
class Events(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    attendees = models.IntegerField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to="media",blank=True, null=True, default='ngong.jpg')                                      

    def __str__(self):
        return self.name