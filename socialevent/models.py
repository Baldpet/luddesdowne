from django.db import models
# Create your models here.



class EventImage(models.Model):
    name = models.CharField(max_length=150)
    image_location = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Events(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    image_location = models.ForeignKey(EventImage, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()


    def __str__(self):
        return self.name