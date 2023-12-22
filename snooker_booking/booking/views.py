from django.shortcuts import render
from .models import Player, SnookerTable, Booking
from .serializers import PlayerSerializer, SnookerTableSerializer, BookingSerializer
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import viewsets
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
@api_view(['POST'])
def login_view(request: Request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'message': 'Method not allowed'}, status=405)




@csrf_exempt
@api_view(['POST'])
def signup_view(request: Request):
    if request.method == 'POST':
        print(request.data.items(), '-------(1)')
        # Extract user data from the request
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        mobile_number = request.data.get('mobile_number')
        age = request.data.get('age')
        birthdate_str = request.data.get('birthdate')  # Assuming birthdate is sent as a string
        gender = request.data.get('gender')
        password = request.data.get('password')

        # Convert birthdate string to a datetime object
        try:
            birthdate = datetime.strptime(birthdate_str, '%d/%m/%Y').date()
        except ValueError:
            return JsonResponse({'message': 'Invalid birthdate format. Please use DD/MM/YYYY.'}, status=400)

        print(first_name,last_name, age, '-------(2)')
        # Create a new user with the provided data
        username = f"{first_name}_{last_name}"        
        # Create UserProfile with additional details
                # Create UserProfile with all collected details
        player = Player.objects.create(
            username=username,
            mobile_number=mobile_number,
            gender=gender,
            first_name=first_name,
            last_name=last_name,
            password=password,
            birth_date=birthdate
        )

        return JsonResponse({'message': 'Signup successful'})
    
    return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
@api_view(['POST'])
def add_table_view(request: Request):
    if request.method == 'POST':
        # Extract table data from the request
        table_type = request.data.get('table_type')
        price = request.data.get('price')

        # Create a new SnookerTable with the provided data
        SnookerTable.objects.create(type=table_type, price=price)

        return JsonResponse({'message': 'Table added successfully'})
    
    return JsonResponse({'message': 'Method not allowed'}, status=405)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class SnookerTableViewSet(viewsets.ModelViewSet):
    queryset = SnookerTable.objects.all()
    serializer_class = SnookerTableSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


