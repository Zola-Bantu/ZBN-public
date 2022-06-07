from django.urls import re_path;
from .api import MosList, MosDetail;

urlpatterns = [re_path(r"^$", MosList.as_view(), name="mosebedisi_list")
             ,re_path(r"(?P<pk>\d+)/$", MosDetail.as_view(), name="mosebedisi_detail")
             ,
             ];
