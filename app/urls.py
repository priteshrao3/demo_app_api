from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('mainslider', views.MainSlidersView, basename='mainslider'),
router.register('studentlist', views.StudentListsView, basename='studentlist'),


urlpatterns = [
    path('', include(router.urls))
]
