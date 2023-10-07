from rest_framework.views import APIView;
from rest_framework.response import Response;
from rest_framework import status;
from .serializer import *;

class MosList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Mosebedisi.objects.all();
        serializer = Mos_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Mos_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class MosDetail(APIView):
    def get_mos(self, pk):
        try:
            model = Mosebedisi.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_mos(pk):
            return Response("No data");
        serializer = Mos_serializer(self.get_mos(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_mos(pk):
            return Response("No data");
        serializer = Mos_serializer(self.get_mos(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_mos(pk):
            return Response("No data");
        model = self.get_mos(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);



class ProfileList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Profile.objects.all();
        serializer = Profile_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Profile_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class ProfileDetail(APIView):
    def get_Profile(self, pk):
        try:
            model = Profile.objects.get(mosebedisi=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Profile(pk):
            return Response("No data");
        serializer = Profile_serializer(self.get_Profile(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Profile(pk):
            return Response("No data");
        serializer = Profile_serializer(self.get_Profile(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Profile(pk):
            return Response("No data");
        model = self.get_Profile(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);


class FriendRequestList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = FriendRequest.objects.all();
        serializer = FriendRequest_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = FriendRequest_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class FriendRequestDetail(APIView):
    def get_FriendRequest(self, pk):
        try:
            model = FriendRequest.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_FriendRequest(pk):
            return Response("No data");
        serializer = FriendRequest_serializer(self.get_FriendRequest(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_FriendRequest(pk):
            return Response("No data");
        serializer = FriendRequest_serializer(self.get_FriendRequest(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_FriendRequest(pk):
            return Response("No data");
        model = self.get_FriendRequest(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);
        
class ContactList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Contact.objects.all();
        serializer = Contact_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Contact_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class ContactDetail(APIView):
    def get_Contact(self, pk):
        try:
            model = Contact.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Contact(pk):
            return Response("No data");
        serializer = Contact_serializer(self.get_Contact(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Contact(pk):
            return Response("No data");
        serializer = Contact_serializer(self.get_Contact(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Contact(pk):
            return Response("No data");
        model = self.get_Contact(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);


class MessageList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Message.objects.all();
        serializer = Message_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Message_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class MessageDetail(APIView):
    def get_Message(self, pk):
        try:
            model = Message.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Message(pk):
            return Response("No data");
        serializer = Message_serializer(self.get_Message(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Message(pk):
            return Response("No data");
        serializer = Message_serializer(self.get_Message(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Message(pk):
            return Response("No data");
        model = self.get_Message(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

class GroupList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Group.objects.all();
        serializer = Group_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Group_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class GroupDetail(APIView):
    def get_Group(self, pk):
        try:
            model = Group.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Group(pk):
            return Response("No data");
        serializer = Group_serializer(self.get_Group(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Group(pk):
            return Response("No data");
        serializer = Group_serializer(self.get_Group(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Group(pk):
            return Response("No data");
        model = self.get_Group(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

class MemberList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Member.objects.all();
        serializer = Member_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Member_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class MemberDetail(APIView):
    def get_Member(self, pk):
        try:
            model = Member.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Member(pk):
            return Response("No data");
        serializer = Member_serializer(self.get_Member(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Member(pk):
            return Response("No data");
        serializer = Member_serializer(self.get_Member(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Member(pk):
            return Response("No data");
        model = self.get_Member(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

class NeedList(APIView):
    def get(self, request):
        model = Need.objects.all();
        serializer = Need_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Need_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class NeedDetail(APIView):
    def get_Need(self, pk):
        try:
            model = Need.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Need(pk):
            return Response("No data");
        serializer = Need_serializer(self.get_Need(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Need(pk):
            return Response("No data");
        serializer = Need_serializer(self.get_Need(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Need(pk):
            return Response("No data");
        model = self.Need(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

class MileStoneList(APIView):
    def get(self, request):
        model = MileStone.objects.all();
        serializer = MileStone_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = MileStone_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class MileStoneDetail(APIView):
    def get_MileStone(self, pk):
        try:
            model = MileStone.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_MileStone(pk):
            return Response("No data");
        serializer = MileStone_serializer(self.get_MileStone(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_MileStone(pk):
            return Response("No data");
        serializer = MileStone_serializer(self.get_MileStone(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_MileStone(pk):
            return Response("No data");
        model = self.get_MileStone(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

#class DependencyList(APIView):

#class DependencyDetail(APIView):

class ResponsibilityList(APIView):
    def get(self, request):
        model = Responsibility.objects.all();
        serializer = Responsibility_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Responsibility_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class ResponsibilityDetail(APIView):
    def get_Responsibility(self, pk):
        try:
            model = Responsibility.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Responsibility(pk):
            return Response("No data");
        serializer = Responsibility_serializer(self.get_Responsibility(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Responsibility(pk):
            return Response("No data");
        serializer = Responsibility_serializer(self.get_Responsibility(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Responsibility(pk):
            return Response("No data");
        model = self.get_Responsibility(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

class CandidatesList(APIView):
    def get(self, request):
        model = Candidates.objects.all();
        serializer = Candidates_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Candidates_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class CandidatesDetail(APIView):
    def get_Candidates(self, pk):
        try:
            model = Candidates.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Candidates(pk):
            return Response("No data");
        serializer = Candidates_serializer(self.get_Candidates(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Candidates(pk):
            return Response("No data");
        serializer = Candidates_serializer(self.get_Candidates(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Candidates(pk):
            return Response("No data");
        model = self.get_Candidates(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

class AchievementList(APIView):
    def get(self, request):
        model = Achievement.objects.all();
        serializer = Achievement_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Achievement_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class AchievementDetail(APIView):
    def get_Achievement(self, pk):
        try:
            model = Achievement.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Achievement(pk):
            return Response("No data");
        serializer = Achievement_serializer(self.get_Achievement(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Achievement(pk):
            return Response("No data");
        serializer = Achievement_serializer(self.get_Achievement(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Achievement(pk):
            return Response("No data");
        model = self.get_Achievement(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

class AchieverList(APIView):
    def get(self, request):
        model = Achiever.objects.all();
        serializer = Achiever_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Achiever_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class AchieverDetail(APIView):
    def get_Achiever(self, pk):
        try:
            model = Achiever.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Achiever(pk):
            return Response("No data");
        serializer = Achiever_serializer(self.get_Achiever(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Achiever(pk):
            return Response("No data");
        serializer = Achiever_serializer(self.get_Achiever(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Achiever(pk):
            return Response("No data");
        model = self.get_Achiever(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

class QualificationRequirementsList(APIView):
    def get(self, request):
        model = QualificationRequirements.objects.all();
        serializer = QualificationRequirements_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = QualificationRequirements_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class QualificationRequirementsDetail(APIView):
    def get_QualificationRequirements(self, pk):
        try:
            model = QualificationRequirements.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_QualificationRequirements(pk):
            return Response("No data");
        serializer = QualificationRequirements_serializer(self.get_QualificationRequirements(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_QualificationRequirements(pk):
            return Response("No data");
        serializer = QualificationRequirements_serializer(self.get_QualificationRequirements(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_QualificationRequirements(pk):
            return Response("No data");
        model = self.get_QualificationRequirements(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);



class LTimeList(APIView):
    def get(self, request):
        model = LTime.objects.all();
        serializer = LTime_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = LTime_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class LTimeDetail(APIView):
    def get_LTime(self, pk):
        try:
            model = LTime.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_LTime(pk):
            return Response("No data");
        serializer = LTime_serializer(self.get_LTime(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_LTime(pk):
            return Response("No data");
        serializer = LTime_serializer(self.get_LTime(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_LTime(pk):
            return Response("No data");
        model = self.get_LTime(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);



class HeaderList(APIView):
    def get(self, request):
        model = Header.objects.all();
        serializer = Header_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Header_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class HeaderDetail(APIView):
    def get_Header(self, pk):
        try:
            model = Header.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Header(pk):
            return Response("No data");
        serializer = Header_serializer(self.get_Header(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Header(pk):
            return Response("No data");
        serializer = Header_serializer(self.get_Header(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Header(pk):
            return Response("No data");
        model = self.get_Header(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

