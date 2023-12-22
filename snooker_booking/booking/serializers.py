from rest_framework import serializers
from .models import Player, SnookerTable, Booking

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class SnookerTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnookerTable
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
