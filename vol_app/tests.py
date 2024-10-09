from django.test import TestCase
from .models import Volunteer, Event

class VolunteerModelTest(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            name='Test Event',
            date='2024-01-01 10:00:00'  # Assuming you have a 'date' field in your Event model
        )

    def test_volunteer_creation(self):
        # Create a Volunteer instance without a User
        volunteer = Volunteer.objects.create(
            event=self.event,
            name='Test Volunteer',  # Assuming you've added a name field to your Volunteer model
            email='testvolunteer@example.com',  # Assuming you've added an email field to your Volunteer model
            role='Coordinator',
            shift_start='2024-01-01 09:00:00',
            shift_end='2024-01-01 11:00:00'
        )
        
        # Check that the volunteer was created correctly
        self.assertEqual(volunteer.name, 'Test Volunteer')
        self.assertEqual(volunteer.email, 'testvolunteer@example.com')  # Check the email
        self.assertEqual(volunteer.event.name, 'Test Event')
        self.assertEqual(volunteer.role, 'Coordinator')
