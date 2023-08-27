from rest_framework.views import APIView;
from rest_framework.response import Response;
from rest_framework import status;
from .serializer import *;

class MMPointList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = MMPoint.objects.all();
        serializer = MMPoint_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = MMPoint_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class MMPointDetail(APIView):
    def get_MMPoint(self, pk):
        try:
            model = MMPoint.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_MMPoint(pk):
            return Response("No data");
        serializer = MMPoint_serializer(self.get_MMPoint(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_MMPoint(pk):
            return Response("No data");
        serializer = MMPoint_serializer(self.get_MMPoint(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_MMPoint(pk):
            return Response("No data");
        model = self.get_MMPoint(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);


class Corre0List(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Corre0.objects.all();
        serializer = Corre0_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Corre0_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class Corre0Detail(APIView):
    def get_Corre0(self, pk):
        try:
            model = Corre0.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Corre0(pk):
            return Response("No data");
        serializer = Corre0_serializer(self.get_Corre0(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Corre0(pk):
            return Response("No data");
        serializer = Corre0_serializer(self.get_Corre0(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Corre0(pk):
            return Response("No data");
        model = self.get_Corre0(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);


class FBMPointList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = FBMPoint.objects.all();
        serializer = FBMPoint_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = FBMPoint_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class FBMPointDetail(APIView):
    def get_FBMPoint(self, pk):
        try:
            model = FBMPoint.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_FBMPoint(pk):
            return Response("No data");
        serializer = FBMPoint_serializer(self.get_FBMPoint(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_FBMPoint(pk):
            return Response("No data");
        serializer = FBMPoint_serializer(self.get_FBMPoint(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_FBMPoint(pk):
            return Response("No data");
        model = self.get_FBMPoint(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);


class Corre1List(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Corre1.objects.all();
        serializer = Corre1_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Corre1_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class Corre1Detail(APIView):
    def get_Corre1(self, pk):
        try:
            model = Corre1.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Corre1(pk):
            return Response("No data");
        serializer = Corre1_serializer(self.get_Corre1(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Corre1(pk):
            return Response("No data");
        serializer = Corre1_serializer(self.get_Corre1(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Corre1(pk):
            return Response("No data");
        model = self.get_Corre1(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);


class LLPointList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = LLPoint.objects.all();
        serializer = LLPoint_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = LLPoint_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class LLPointDetail(APIView):
    def get_LLPoint(self, pk):
        try:
            model = LLPoint.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_LLPoint(pk):
            return Response("No data");
        serializer = LLPoint_serializer(self.get_LLPoint(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_LLPoint(pk):
            return Response("No data");
        serializer = LLPoint_serializer(self.get_LLPoint(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_LLPoint(pk):
            return Response("No data");
        model = self.get_LLPoint(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);


class LLPositionList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = LLPosition.objects.all();
        serializer = LLPosition_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = LLPosition_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class LLPositionDetail(APIView):
    def get_LLPosition(self, pk):
        try:
            model = LLPosition.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_LLPosition(pk):
            return Response("No data");
        serializer = LLPosition_serializer(self.get_LLPosition(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_LLPosition(pk):
            return Response("No data");
        serializer = LLPosition_serializer(self.get_LLPosition(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_LLPosition(pk):
            return Response("No data");
        model = self.get_LLPosition(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);


class HeaderList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
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


class EventList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Event.objects.all();
        serializer = Event_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Event_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class EventDetail(APIView):
    def get_Event(self, pk):
        try:
            model = Event.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Event(pk):
            return Response("No data");
        serializer = Event_serializer(self.get_Event(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Event(pk):
            return Response("No data");
        serializer = Event_serializer(self.get_Event(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Event(pk):
            return Response("No data");
        model = self.get_Event(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);


class ReminderList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Reminder.objects.all();
        serializer = Reminder_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Reminder_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class ReminderDetail(APIView):
    def get_Reminder(self, pk):
        try:
            model = Reminder.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Reminder(pk):
            return Response("No data");
        serializer = Reminder_serializer(self.get_Reminder(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Reminder(pk):
            return Response("No data");
        serializer = Reminder_serializer(self.get_Reminder(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Reminder(pk):
            return Response("No data");
        model = self.get_Reminder(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);


class TaskList(APIView): # Inherits from the APIView class.
    # Gets data from the database.
    def get(self, request):
        model = Task.objects.all();
        serializer = Task_serializer(model, many=True);
        return Response(serializer.data);

    def post(self, request):
        serializer = Task_serializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST);

class TaskDetail(APIView):
    def get_Task(self, pk):
        try:
            model = Task.objects.get(id=pk);
            return model;
        except Exception as e:
            print(e);
            return;
    
    def get(self, requests, pk):
        if not self.get_Task(pk):
            return Response("No data");
        serializer = Task_serializer(self.get_Task(pk));
        return Response(serializer.data);
        
    def put(self, requests, pk):
        if not self.get_Task(pk):
            return Response("No data");
        serializer = Task_serializer(self.get_Task(pk), data=requests.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS);
        
    def delete(self, requests, pk):
        if not self.get_Task(pk):
            return Response("No data");
        model = self.get_Task(pk);
        model.delete();
        return Response(status=status.HTTP_204_NO_CONTENT);

