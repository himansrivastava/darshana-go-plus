from django.test import TestCase

from institute.models import Institute


class TestData(TestCase):
    """Common set up for Institute models and api tests"""

    @classmethod
    def setUpTestData(cls):
        """Create base data for test"""

        # create institute object
        cls.institute = Institute.objects.create(
            id="INS001",
            name="Test Institute",
            address="Test Address",
            contact_person="Test Contact Person",
            status="Active",
        )
