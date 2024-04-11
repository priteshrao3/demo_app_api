from app.models import MainSlider, StudentList
from app.serializers import MainSlider_serializer, StudentListSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny



class MainSlidersView(viewsets.ModelViewSet):
    queryset = MainSlider.objects.all()
    serializer_class = MainSlider_serializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]




class StudentListsView(viewsets.ModelViewSet):
    queryset = StudentList.objects.all()
    serializer_class = StudentListSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
