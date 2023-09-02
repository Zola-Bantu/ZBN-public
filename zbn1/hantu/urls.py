from . import views
from django.urls import re_path, include;
from .api import MMPointList, MMPointDetail, Corre0List, Corre0Detail, FBMPointList, FBMPointDetail, Corre1List, Corre1Detail, LLPointList, LLPointDetail, LLPositionList, LLPositionDetail, HeaderList, HeaderDetail, EventList, EventDetail, ReminderList, ReminderDetail, TaskList, TaskDetail;# MosList, MosDetail, ProfileList, ProfileDetail,MessageDetail,MessageList, GroupDetail, GroupList, MemberDetail, MemberList

urlpatterns = [re_path(r"^$", views.sitemap, name="sitemap"),
            re_path(r"^mmpnt/$", MMPointList.as_view(), name="mmpoint_list"),
            re_path(r"^mmpnt/(?P<pk>\d+)/$", MMPointDetail.as_view(), name="mmpoint_detail"),
            re_path(r"^cor0/$", Corre0List.as_view(), name="corre0_list"),
            re_path(r"^cor0/(?P<pk>\d+)/$", Corre0Detail.as_view(), name="corre0_detail"),
            re_path(r"^fbmpnt/$", FBMPointList.as_view(), name="fbmpoint_list"),
            re_path(r"^fbmpnt/(?P<pk>\d+)/$", FBMPointDetail.as_view(), name="fbmpoint_detail"),
            re_path(r"^cor1/$", Corre1List.as_view(), name="corre1_list"),
            re_path(r"^cor1/(?P<pk>\d+)/$", Corre1Detail.as_view(), name="corre1_detail"),
            re_path(r"^llpnt/$", LLPointList.as_view(), name="llpoint_list"),
            re_path(r"^llpnt/(?P<pk>\d+)/$", LLPointDetail.as_view(), name="llpoint_detail"),
            re_path(r"^llpos/$", LLPositionList.as_view(), name="llposition_list"),
            re_path(r"^llpos/(?P<pk>\d+)/$", LLPositionDetail.as_view(), name="llposition_detail"),
            re_path(r"^head/$", HeaderList.as_view(), name="header_list"),
            re_path(r"^head/(?P<pk>\d+)/$", HeaderDetail.as_view(), name="header_detail"),
            re_path(r"^event/$", EventList.as_view(), name="event_list"),
            re_path(r"^event/(?P<pk>\d+)/$", EventDetail.as_view(), name="event_detail"),
            re_path(r"^rem/$", ReminderList.as_view(), name="reminder_list"),
            re_path(r"^rem/(?P<pk>\d+)/$", ReminderDetail.as_view(), name="reminder_detail"),
            re_path(r"^task/$", TaskList.as_view(), name="task_list"),
            re_path(r"^task/(?P<pk>\d+)/$", TaskDetail.as_view(), name="task_detail"),
            ];
