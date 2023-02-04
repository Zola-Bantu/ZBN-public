from . import views
from django.urls import re_path;
from .api import MosList, MosDetail, ProfileList, ProfileDetail

urlpatterns = [re_path(r"^$", views.monyako, name="monyako"), #login page
            re_path(r"^mos/$", MosList.as_view(), name="mosebedisi_list"),
            re_path(r"^mos/(?P<pk>\d+)/$", MosDetail.as_view(), name="mosebedisi_detail"),
            re_path(r"^prof/$", ProfileList.as_view(), name="profile_list"),
            re_path(r"^prof/(?P<pk>\d+)/$", ProfileDetail.as_view(), name="profile_detail"),
            ];
