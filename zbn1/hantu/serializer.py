from rest_framework import serializers;
from .models import *;

class MMPoint_serializer(serializers.ModelSerializer):
    class Meta:
        model = MMPoint; # Use our defined model.
        fields = "__all__"; # Brings all fields from the database.

class Corre0_serializer(serializers.ModelSerializer):
    class Meta:
        model = Corre0;
        fields = "__all__";

class FBMPoint_serializer(serializers.ModelSerializer):
    class Meta:
        model = FBMPoint;
        fields = "__all__";

class Corre1_serializer(serializers.ModelSerializer):
    class Meta:
        model = Corre1;
        fields = "__all__";

class LLPoint_serializer(serializers.ModelSerializer):
    class Meta:
        model = LLPoint;
        fields = "__all__";

class LLPosition_serializer(serializers.ModelSerializer):
    class Meta:
        model = LLPosition;
        fields = "__all__";

class Header_serializer(serializers.ModelSerializer):
    class Meta:
        model = Header;
        fields = "__all__";

class Event_serializer(serializers.ModelSerializer):
    class Meta:
        model = Event;
        fields = "__all__";

class Reminder_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder;
        fields = "__all__";

class Task_serializer(serializers.ModelSerializer):
    class Meta:
        model = Task;
        fields = "__all__";

