"""Serializers for the Institute API."""
import logging

from django.conf import settings
from rest_framework import serializers

from .models import (
    Institute,
)

logger = logging.getLogger(__name__)


class InstituteSerializer(serializers.ModelSerializer):
    """Serializer for the Institute model."""

    class Meta:
        model = Institute
        fields = "__all__"

    def update(self, instance, validated_data):

        logger.info("Info Starting update ")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        logger.info("Info Ending update ")
        return instance
