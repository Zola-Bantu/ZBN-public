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

class Group_serializer(serializers.ModelSerializer):
    class Meta:
        model = Group;
        fields = "__all__";

class Member_serializer(serializers.ModelSerializer):
    class Meta:
        model = Member;
        fields = "__all__";

class Need_serializer(serializers.ModelSerializer):
    class Meta:
        model = Need;
        fields = "__all__";

class MileStone_serializer(serializers.ModelSerializer):
    class Meta:
        model = MileStone;
        fields = "__all__";
"""
class Dependency_serializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency;
        fields = "__all__";
"""
class Responsibility_serializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility;
        fields = "__all__";

class Candidates_serializer(serializers.ModelSerializer):
    class Meta:
        model = Candidates;
        fields = "__all__";

class Achievement_serializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement;
        fields = "__all__";

class Achiever_serializer(serializers.ModelSerializer):
    class Meta:
        model = Achiever;
        fields = "__all__";

class QualificationRequirements_serializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationRequirements;
        fields = "__all__";

class LTime_serializer(serializers.ModelSerializer):
    class Meta:
        model = LTime;
        fields = "__all__";


class Header_serializer(serializers.ModelSerializer):
    class Meta:
        model = Header;
        fields = "__all__";
