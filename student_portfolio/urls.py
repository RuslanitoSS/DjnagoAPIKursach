from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from portfolio.views import StudentViewSet, ProjectViewSet, EventViewSet
from django.urls import path


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
    
   
