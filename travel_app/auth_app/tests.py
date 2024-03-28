from django.test import TestCase
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

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
        ''' Test if no data passed to the User serializer '''

        obj = {
            "username": "ashish3",
            "password": "ganesh123",
            "email": "as3@gmail.com" 
            }
        serializer = UserSerializer(data=obj) 
        self.assertFalse(serializer.is_valid())

    def test_user_serializer_password(self):
        '''tset for password and confirm password '''

        obj =  {
                "username": "ashish3",
                "password": "ganesh123",
                "confirm_password": "ganesh123",
                "email": "as3@gmail.com" 
                }
        serializer = UserSerializer(data=obj)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['password'], serializer.validated_data['confirm_password'])


class UserAPITestCase(TestCase):
    '''test case for user create in User model'''

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='ashish7', password='password',
                                    email='as3@gmail.com')

    def test_create_user(self):
        ''' Api Testcase for testing user creation '''
        
        url = '/user/create/'
        data = {'username': 'ashish9', 'password': 'password', 'email':"as3@gmail.com",
                'confirm_password':'password'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        


