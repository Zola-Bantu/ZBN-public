from rest_framework import serializers;
from .models import *;

class Mos_serializer(serializers.ModelSerializer):
    class Meta:
        model = Mosebedisi; # Use our defined model.
        fields = "__all__"; # Brings all fields from the database.

class Profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile;
        fields = "__all__";

class Message_serializer(serializers.ModelSerializer):
    class Meta:
        model = Message;
        fields = "__all__";