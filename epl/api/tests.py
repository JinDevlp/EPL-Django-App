from user.models import Profile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

class ProfileTests(APITestCase):
    def test_register(self):

        url = reverse('teamsAPI')
        data = {''}

