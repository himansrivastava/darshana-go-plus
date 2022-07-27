"""Tests for Institute api"""
from django.urls import resolve, reverse
from rest_framework.test import APIClient
from rest_framework import status

from institute import views

from .test_base import TestData

INSTITUTE_URL = reverse("instituteapi:institute-list")


def get_detail_url(pk):
    """Return the detail url for the given pk"""
    return reverse("instituteapi:institute-detail", args=[pk])


class InstituteAPITest(TestData):
    """Test the Institute API"""

    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            "id": "INS002",
            "name": "Test Institute 2",
            "address": "Test Address 2",
            "contact_person": "Test Contact Person 2",
            "status": "Active",
        }
        self.put_payload = {
            "id": "INS001",
            "name": "Test Institute Edited",
            "address": "Test Address Edited",
            "contact_person": "Test Contact Person...",
            "status": "Active",
        }
        self.patch_payload = {
            "status": "InActive",
        }

    # Test retrieving a list of institutes
    def test_list_institutes(self):
        """Test retrieving a list of institutes"""
        res = self.client.get(INSTITUTE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.json()), 1)

    # Test retrieving a institute
    def test_retrieve_institute(self):
        """Test retrieving a institute"""
        url = get_detail_url(self.institute.pk)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # Test creating a salesorder
    def test_create_institute(self):
        """Test creating a institute"""
        res = self.client.post(INSTITUTE_URL, self.valid_payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.json()["id"], "INS002")

    # Test updating a salesorder with valid payload
    def test_update_institute(self):
        """Test updating a institute with valid payload"""
        url = get_detail_url(self.institute.pk)
        res = self.client.put(url, self.put_payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()["name"], "Test Institute Edited")

    # Test partial update a salesorder with valid payload
    def test_partial_update_institute(self):
        """Test partial update a institute with valid payload"""
        url = get_detail_url(self.institute.pk)
        res = self.client.patch(url, self.patch_payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()["status"], "InActive")

    # Test deleting a salesorder
    def test_delete_institute(self):
        """Test deleting a institute"""
        url = get_detail_url(self.institute.pk)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
