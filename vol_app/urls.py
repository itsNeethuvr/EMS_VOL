from django.urls import path
from .views import VolunteerListCreateAPIView, volunteer_management_view

urlpatterns = [
    path('api/volunteers/', VolunteerListCreateAPIView.as_view(), name='volunteer-list-create'),

    path('', volunteer_management_view, name='volunteer-management'),  # The main view
]
print("URLs loaded:", urlpatterns)  # Add this line for debugging