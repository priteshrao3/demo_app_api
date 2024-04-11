from django.db import models

# Create your models here.
class MainSlider(models.Model):
          SliderImage = models.ImageField(upload_to='sliderimg', null=True, blank=True)


class StudentList(models.Model):
        Student_Pic = models.ImageField(upload_to='Studnet_Pic', null=True, blank=True)
        Student_Name = models.CharField(max_length=50)
        Student_Description = models.CharField(max_length=500, null=True, blank=True)
        Student_Marks = models.IntegerField(null=True, blank=True)