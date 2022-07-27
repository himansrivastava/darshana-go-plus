from rest_framework import viewsets

from .models import Institute
from institute import serializers


class InstituteViewSet(viewsets.ModelViewSet):
    """API endpoint that allows to view, edit, create and delete Institute"""

    queryset = Institute.objects.all()
    serializer_class = serializers.InstituteSerializer
