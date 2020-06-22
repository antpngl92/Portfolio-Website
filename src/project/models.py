from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=120)
    project_description = models.CharField(max_length=400)
    project_link = models.CharField(max_length=500)
    project_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.project_name
    