from django.contrib import admin
from app.models import MainSlider, StudentList

# Register your models here.
@admin.register(MainSlider)
class MainSlider(admin.ModelAdmin):
          list_display = ['id', 'SliderImage']



@admin.register(StudentList)
class StudentList(admin.ModelAdmin):
        list_display = ['id', 'Student_Pic' ,'Student_Name', 'Student_Description', 'Student_Marks']