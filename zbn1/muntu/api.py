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

"""
class NeedList(APIView):

class NeedDetail(APIView):

class MileStoneList(APIView):

class MileStoneDetail(APIView):

class DependencyList(APIView):

class DependencyDetail(APIView):

class ResponsibilityList(APIView):

class ResponsibilityDetail(APIView):

class CandidatesList(APIView):

class CandidatesDetail(APIView):

class QualificationRequirementsList(APIView):

class QualificationRequirementsDetail(APIView):

class AchievementList(APIView):

class AchievementDetail(APIView):

class AchieverList(APIView):

class AchieverDetail(APIView):

"""



