from django.test import TestCase
from .serializers import DestinationSerializer

class DestinationSerializerTestCase(TestCase):
    def test_destination_data(self):
        ''' Test for valid data passed to the destination serializer '''

        obj =  {
                "name": "ganpatipule",
                "country": "India",
                "description": "famous ganapati temple",
                "best_time_to_visit": "at morning time.",
                "category": "Beach",
                "image_url": "https://example.com/image.jpg"
                }
        serializer = DestinationSerializer(data=obj)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serialize_data(self):
        ''' Test for invalid data passed to the destination serializer '''

        obj =  {
                "name": "ganpatipule",
                "country": "India123",
                "description": "famous ganapati temple",
                "best_time_to_visit": "at morning time.",
                "category": "Beach",
                "image_url": "https://example.com/image.jpg"
                }
        serializer = DestinationSerializer(data=obj) 
        self.assertFalse(serializer.is_valid())

    
