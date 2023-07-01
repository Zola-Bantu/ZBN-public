from . import views
from django.urls import re_path, include;
from .api import MosList, MosDetail, ProfileList, ProfileDetail,MessageDetail,MessageList, GroupDetail, GroupList, MemberDetail, MemberList

urlpatterns = [re_path(r"^$", views.sitemap, name="sitemap"),
            ];
