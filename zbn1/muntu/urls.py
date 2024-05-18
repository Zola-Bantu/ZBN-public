from . import views;
from django.urls import re_path, include;
from .api import MosList, MosDetail, FriendRequestList, FriendRequestDetail, ContactList, ContactDetail, ProfileList, ProfileDetail,MessageDetail,MessageList, GroupDetail, GroupList, MemberDetail, MemberList#, NeedList, NeedDetail, MileStoneList, MileStoneDetail, ResponsibilityList, ResponsibilityDetail, CandidatesList, CandidatesDetail, AchievementList, AchievementDetail, AchieverList, AchieverDetail, QualificationRequirementsList, QualificationRequirementsDetail, LTimeList, LTimeDetail, HeaderList, HeaderDetail; #, DependencyList, DependencyDetail
               
urlpatterns = [re_path(r"^$", views.sitemap, name="sitemap"),
            re_path(r"^chat/", views.chat, name="chat"),
            re_path(r"^mos/$", MosList.as_view(), name="mosebedisi_list"),
            re_path(r"^mos/(?P<pk>\d+)/$", MosDetail.as_view(), name="mosebedisi_detail"),            
            re_path(r"^freq/$", FriendRequestList.as_view(), name="friendrequest_list"),
            re_path(r"^freq/(?P<pk>\d+)/$", FriendRequestDetail.as_view(), name="friendrequest_detail"),
            re_path(r"^con/$", ContactList.as_view(), name="contact_list"),
            re_path(r"^con/(?P<pk>\d+)/$", ContactDetail.as_view(), name="contact_detail"),            
            re_path(r"^prof/$", ProfileList.as_view(), name="profile_list"),
            re_path(r"^prof/(?P<pk>\d+)/$", ProfileDetail.as_view(), name="profile_detail"),
            re_path(r"^mes/$", MessageList.as_view(), name="message_list"),
            re_path(r"^mes/(?P<pk>\d+)/$", MessageDetail.as_view(), name="message_detail"),
            re_path(r"^grp/$", GroupList.as_view(), name="group_list"),
            re_path(r"^grp/(?P<pk>\d+)/$", GroupDetail.as_view(), name="group_detail"),
            re_path(r"^mem/$", MemberList.as_view(), name="member_list"),
            re_path(r"^mem/(?P<pk>\d+)/$", MemberDetail.as_view(), name="member_detail"),
            #re_path(r"^need/$", NeedList.as_view(), name="need_list"),
            #re_path(r"^need/(?P<pk>\d+)/$", NeedDetail.as_view(), name="need_detail"),
            #re_path(r"^mst/$", MileStoneList.as_view(), name="miletone_list"),
            #re_path(r"^mst/(?P<pk>\d+)/$", MileStoneDetail.as_view(), name="miletone_detail"),
            #re_path(r"^dep/$", DependencyList.as_view(), name="dependency_list"),
            #re_path(r"^dep/(?P<pk>\d+)/$", DependencyDetail.as_view(), name="dependency_detail"),
            #re_path(r"^resp/$", ResponsibilityList.as_view(), name="responsibility_list"),
            #re_path(r"^resp/(?P<pk>\d+)/$", ResponsibilityDetail.as_view(), name="responsibility_detail"),
            #re_path(r"^cand/$", CandidatesList.as_view(), name="candidates_list"),
            #re_path(r"^cand/(?P<pk>\d+)/$", CandidatesDetail.as_view(), name="candidates_detail"),
            #re_path(r"^ach/$", AchievementList.as_view(), name="achievement_list"),
            #re_path(r"^ach/(?P<pk>\d+)/$", AchievementDetail.as_view(), name="achievement_detail"),
            #re_path(r"^achr/$", AchieverList.as_view(), name="achiever_list"),
            #re_path(r"^achr/(?P<pk>\d+)/$", AchieverDetail.as_view(), name="achiever_detail"),
            #re_path(r"^qreq/$", QualificationRequirementsList.as_view(), name="qualificationrequirements_list"),
            #re_path(r"^qreq/(?P<pk>\d+)/$", QualificationRequirementsDetail.as_view(), name="qualificationrequirements_detail"),
            #re_path(r"^ltime/$", LTimeList.as_view(), name="ltime_list"),
            #re_path(r"^ltime/(?P<pk>\d+)/$", LTimeDetail.as_view(), name="ltime_detail"),
            #re_path(r"^head/$", HeaderList.as_view(), name="header_list"),
            #re_path(r"^head/(?P<pk>\d+)/$", HeaderDetail.as_view(), name="header_detail"),
            #re_path(r"^secure/", include('entrance.urls')), #login page
            ];
