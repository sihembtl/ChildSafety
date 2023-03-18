from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from .models import Child, Parent, SocialMedia, Activity, Schedule, Devices , App , Location


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id', 'first_name', 'date_of_birth', 'parent']

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['id', 'first_name', 'last_name', 'date_of_birth']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'first_name', 'last_name', 'child']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'first_name', 'last_name', 'child']

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'name','child']

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ['id', 'name','child']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name' , 'child']

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'name', 'child']
