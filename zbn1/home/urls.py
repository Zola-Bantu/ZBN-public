from . import views
from django.urls import re_path;
from .api import MosList, MosDetail;

urlpatterns = [re_path(r"^$", views.monyako, name="monyako"), #login page
            re_path(r"^mos/$", MosList.as_view(), name="mosebedisi_list"),
            re_path(r"^mos/(?P<pk>\d+)/$", MosDetail.as_view(), name="mosebedisi_detail"),
            ];
