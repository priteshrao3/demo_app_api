from app.models import MainSlider, StudentList
from rest_framework import serializers

class MainSlider_serializer(serializers.ModelSerializer):

    class Meta:
        model = MainSlider
        fields = ['id', 'SliderImage']




class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentList
        fields = ['id',  'Student_Pic', 'Student_Name', 'Student_Description', 'Student_Marks']