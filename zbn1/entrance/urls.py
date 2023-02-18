from . import views
from django.urls import re_path, include;


urlpatterns = [
            re_path(r"^$", views.secure, name="secure"),#login page
            ];
