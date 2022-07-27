"""Tests for the Institute app models."""
from .test_base import TestData
from institute.models import Institute


class TestInstituteModel(TestData):
    """Test for Institute model"""

    def test_institute_model_created_with_correct_data(self):
        """Test Institute object is created with correct data"""

        self.assertEqual(self.institute.id, "INS001")
        self.assertEqual(self.institute.name, "Test Institute")
        self.assertEqual(self.institute.address, "Test Address")
        self.assertEqual(self.institute.contact_person, "Test Contact Person")
        self.assertEqual(self.institute.status, "Active")
