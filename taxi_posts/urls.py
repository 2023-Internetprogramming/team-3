from django.urls import path
from .views import ride_list, ride_detail, ride_create

urlpatterns = [
    path('rides/', ride_list, name='ride_list'),
    path('rides/<int:ride_id>/', ride_detail, name='ride_detail'),
    path('rides/new/', ride_create, name='ride_create'),
]