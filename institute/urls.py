"""URLs for the institue api"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from institute import views

app_name = "instituteapi"

router = DefaultRouter()

router.register("", views.InstituteViewSet, basename="institute")

urlpatterns = [
    path("", include(router.urls)),
]
