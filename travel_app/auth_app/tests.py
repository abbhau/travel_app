from django.test import TestCase
from .serializers import UserSerializer

# Create your tests here.
class UserSerializerTestCase(TestCase):
    def test_user_data(self):
        ''' Test for valid data passed to the User serializer '''

        obj =  {
                "username": "ashish3",
                "password": "ganesh123",
                "confirm_password": "ganesh123",
                "email": "as3@gmail.com" 
                }
        serializer = UserSerializer(data=obj)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serialize_data(self):
        ''' Test for invalid data or no data passed to the User serializer '''

        obj = {
            "username": "ashish3",
            "password": "ganesh123",
            "confirm_password": "ganesh123",
            "email": "as3@gmail.com" 
            }
        serializer = UserSerializer(data=obj) 
        self.assertFalse(serializer.is_valid())

