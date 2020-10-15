from django.test import TestCase
from django.contrib.auth.models import User
from .models import AdminHod
# Create your tests here.
class userCreate(TestCase):
    def setUp(self):
        user1=User(username='jamall',email='jamal@hh.fd')
        user1.is_staff=True
        user1.set_password='jamal123'
        user1.is_superuser=True
        user1.save()
        
        usera=AdminHod(user=user1)
        self.usera=usera
        self.user1=user1

    def test_user_pass(self):
        self.user1.check_password('jamal123')

    def test_user_is_admin(self):
        user2=AdminHod.subjects.filter(user=self.usera)
        self.assertEqual(user2,usera)