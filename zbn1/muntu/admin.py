from django.contrib import admin;
from .models import Mosebedisi, Profile, FriendRequest, Contact, Message, Group, Member, Need, MileStone, Responsibility, Candidates, Achievement, Achiever, QualificationRequirements, LTime, Header; #, Dependency

# Register your models here.
admin.site.register(Mosebedisi);
admin.site.register(Profile);
admin.site.register(FriendRequest);
admin.site.register(Contact);
admin.site.register(Message);
admin.site.register(Group);
admin.site.register(Member);
admin.site.register(Need);
admin.site.register(MileStone);
#admin.site.register(Dependency);
admin.site.register(Responsibility);
admin.site.register(Candidates);
admin.site.register(Achievement);
admin.site.register(Achiever);
admin.site.register(QualificationRequirements);
admin.site.register(LTime);
admin.site.register(Header);
