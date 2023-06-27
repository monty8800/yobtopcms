from django.urls import path, include
from rest_framework import routers

from zip import views

router = routers.DefaultRouter()
router.register(r'zipcode', views.ZipCodeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
