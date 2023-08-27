from . import views
from django.urls import re_path, include;
from .api import MMPoint, Corre0, FBMPoint, Corre1, LLPoint, LLPosition, Header, Event, Reminder, Task;# MosList, MosDetail, ProfileList, ProfileDetail,MessageDetail,MessageList, GroupDetail, GroupList, MemberDetail, MemberList

urlpatterns = [re_path(r"^$", views.sitemap, name="sitemap"),
            re_path(r"^qreq/$", MMPointList.as_view(), name="mmpoint_list"),
            re_path(r"^qreq/(?P<pk>\d+)/$", MMPointDetail.as_view(), name="mmpoint_detail"),
            re_path(r"^qreq/$", Corre0List.as_view(), name="corre0_list"),
            re_path(r"^qreq/(?P<pk>\d+)/$", Corre0Detail.as_view(), name="corre0_detail"),
            re_path(r"^qreq/$", FBMPointList.as_view(), name="fbmpoint_list"),
            re_path(r"^qreq/(?P<pk>\d+)/$", FBMPointDetail.as_view(), name="fbmpoint_detail"),
            re_path(r"^qreq/$", Corre1List.as_view(), name="corre1_list"),
            re_path(r"^qreq/(?P<pk>\d+)/$", Corre1Detail.as_view(), name="corre1_detail"),
            re_path(r"^qreq/$", LLPointList.as_view(), name="llpoint_list"),
            re_path(r"^qreq/(?P<pk>\d+)/$", LLPointDetail.as_view(), name="llpoint_detail"),
            re_path(r"^qreq/$", LLPositionList.as_view(), name="llposition_list"),
            re_path(r"^qreq/(?P<pk>\d+)/$", LLPositionDetail.as_view(), name="llposition_detail"),
            re_path(r"^qreq/$", HeaderList.as_view(), name="header_list"),
            re_path(r"^qreq/(?P<pk>\d+)/$", HeaderDetail.as_view(), name="header_detail"),
            re_path(r"^qreq/$", EventList.as_view(), name="event_list"),
            re_path(r"^qreq/(?P<pk>\d+)/$", EventDetail.as_view(), name="event_detail"),
            re_path(r"^qreq/$", ReminderList.as_view(), name="reminder_list"),
            re_path(r"^qreq/(?P<pk>\d+)/$", ReminderDetail.as_view(), name="reminder_detail"),
            re_path(r"^qreq/$", TaskList.as_view(), name="tsask_list"),
            re_path(r"^qreq/(?P<pk>\d+)/$", TaskDetail.as_view(), name="task_detail"),
            ];
