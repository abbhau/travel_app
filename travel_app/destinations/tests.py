from django.test import TestCase
from .serializers import DestinationSerializer
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from .models import Destination
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse


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


class DestinationAPITestCase(APITestCase):
    def setUp(self):
        '''setup for the Apitestcase'''
        self.user = User.objects.create_user(username='testuser', email='test@example.com',
                                              password='password')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.dest1 = Destination.objects.create(name='Destination 1', country='Country 1', 
                                description='Description 1', best_time_to_visit='Time 1', 
                                category='Beach', image_url='http://example.com/image1.jpg')
        self.dest2 = Destination.objects.create(name='Destination 2', country='Country 2',
                             description='Description 2', best_time_to_visit='Time 2', 
                           category='Mountain', image_url='http://example.com/image2.jpg')

    def test_create_destination_authenticated(self):
        '''Api test case for creating a Destination record'''

        url = reverse('destination-create')
        data = {'name': 'New Destination', 'country': 'Country', 
                'description': 'New Description', 'best_time_to_visit': 'New Time', 
                'category': 'City', 'image_url': 'http://example.com/image3.jpg'}
        
        # Include the token in the request headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_destination_list(self):
        '''Api test case for fetching all Destination record'''

        url = reverse('destination-list')
        
        # Include the token in the request headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_destination_retrive(self):
        '''Api test case for retriving specific Destination record'''

        url = reverse('destination-detail', kwargs={'pk': self.dest1.pk})
        
        # Include the token in the request headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_destination(self):
        '''Api test Case for method not allowed '''

        url = reverse('destination-list')
        data = {'name': 'New Destination', 'country': 'New Country', 
                'description': 'New Description', 'best_time_to_visit': 'New Time', 
               'category': 'City', 'image_url': 'http://example.com/image3.jpg'}
        # Include the token in the request headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_destination_delete(self):
        '''Api test case for deleting specific Destination record'''

        url = reverse('destination-delete', kwargs={'pk': self.dest1.pk})
        
        # Include the token in the request headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    




    