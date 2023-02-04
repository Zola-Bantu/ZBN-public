from django.contrib import admin;
from .models import Mosebedisi, Profile, Message, Group, Member;

# Register your models here.
admin.site.register(Mosebedisi);
admin.site.register(Profile);
admin.site.register(Message);
admin.site.register(Group);
admin.site.register(Member);
