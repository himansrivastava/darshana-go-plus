"""Serializers for the Institute API."""

from rest_framework import serializers

from .models import (
    Institute,
)


class InstituteSerializer(serializers.ModelSerializer):
    """Serializer for the Institute model."""

    class Meta:
        model = Institute
        fields = "__all__"
