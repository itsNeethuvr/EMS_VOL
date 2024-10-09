from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Volunteer
from .serializers import VolunteerSerializer
import logging
"""from django.http import HttpResponse

def api_documentation_view(request):
    return HttpResponse(
        <h1>API Documentation</h1>
        <h2>Available Endpoints</h2>
        <ul>
            <li><strong>GET /api/volunteers/</strong> - Retrieve a list of all volunteers</li>
            <li><strong>POST /api/volunteers/</strong> - Register a new volunteer</li>
        </ul>
        <p>Please start your requests at /api/.</p>
    )"""


logger = logging.getLogger(__name__)

def volunteer_management_view(request):
    return render(request, 'vol_app/volunteers.html')

"""class VolunteerListCreateAPIView(APIView):
    # No permission classes needed for open access
    # permission_classes = [IsAuthenticated]  

    def get(self, request):
        print("GET request received")  # Debugging statement
        volunteers = Volunteer.objects.all()
        serializer = VolunteerSerializer(volunteers, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        role = request.data.get('role')
        shift_start = request.data.get('shift_start')
        shift_end = request.data.get('shift_end')
        event_id = request.data.get('event')  # Get the event ID

        # Validate input fields
        if not all([name, email, role, shift_start, shift_end]):
            return Response({'detail': 'All fields (name, email, role, shift start, shift end) must be provided.'}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare volunteer data
        volunteer_data = {
            'name': name,
            'email': email,
            'role': role,
            'shift_start': shift_start,
            'shift_end': shift_end,
        }

        # If an event ID is provided, validate it
        if event_id:
            try:
                event = Event.objects.get(id=event_id)  # Get the event object
                volunteer_data['event'] = event.id
            except Event.DoesNotExist:
                return Response({'detail': 'Event not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Validate and save the volunteer data
        serializer = VolunteerSerializer(data=volunteer_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""
class VolunteerListCreateAPIView(APIView):
    def get(self, request):
        volunteers = Volunteer.objects.all()
        serializer = VolunteerSerializer(volunteers, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        role = request.data.get('role')
        shift_start = request.data.get('shift_start')
        shift_end = request.data.get('shift_end')
        event_id = request.data.get('event')  # Get the event ID

        # Validate input fields
        if not all([name, email, role, shift_start, shift_end]):
            return Response({'detail': 'All fields (name, email, role, shift start, shift end) must be provided.'}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare volunteer data
        volunteer_data = {
            'name': name,
            'email': email,
            'role': role,
            'shift_start': shift_start,
            'shift_end': shift_end,
        }

        # If an event ID is provided, validate it
        """if event_id:
            try:
                event = Event.objects.get(id=event_id)  # Get the event object
                volunteer_data['event'] = event.id
            except Event.DoesNotExist:
                return Response({'detail': 'Event not found.'}, status=status.HTTP_404_NOT_FOUND)"""

        # Validate and save the volunteer data
        serializer = VolunteerSerializer(data=volunteer_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)