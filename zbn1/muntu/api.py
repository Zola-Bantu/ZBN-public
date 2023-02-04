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
