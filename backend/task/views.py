from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import User, List, MyTask
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, ListSerializer, MyTaskSerializer, LoginSerializer, ExpandListSerializer

# Create your views here.

#---------------Class Based Views--------------------
# class UserList(APIView):
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---------------Viewset Throwing Error---------------
class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data = data)
            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['password']

                user = authenticate(email = email, password = password)

                if user is None:
                    return Response({"bkl": "Bohat bada bkl hai"})
                
                refresh = RefreshToken.for_user(user)

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'id': user.id,
                })

            return Response({"message": "Bohat chota bkl hai"})

        except Exception as e:
            return Response({"message": "Exception!"})


class UserViewSet(ViewSet):
    def create(self, request):
        # serializer = UserSerializer(data = request.data)
        print(request.data)

        User.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        return Response(status=status.HTTP_200_OK)
    
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many = True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk):
        try:
            queryset = User.objects.get(pk = pk)
        except User.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(queryset)
        return Response(serializer.data)
    
    
    
class ListViewSet(ViewSet):
    def create(self, request):
        serializer = ListSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors':serializer.errors,})
    
    def list(self, request):
        queryset = List.objects.all()
        serializer = ListSerializer(queryset, many = True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk):
        try:
            queryset = List.objects.get(pk = pk)
        except List.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = ListSerializer(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk):
        id = pk
        task = List.objects.get(pk=id)
        serializer = ListSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, pk= None):
        try:
            obj = List.objects.get(pk=pk)
            obj.delete()
            return Response(status=status.HTTP_200_OK)
        except List.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
    
    def user_list(self, request, user_id):
        queryset = List.objects.filter(user_id = user_id).all()
        serializer = ListSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def expand(self, request, pk=None):
        try:
            queryset = List.objects.get(pk=pk)
        except List.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExpandListSerializer(queryset)
        return Response(serializer.data)
    
        
    
class TaskViewSet(ViewSet):
    def create(self, request):
        serializer = MyTaskSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors,})
    
    def list(self, request):
        queryset = MyTask.objects.all()
        serializer = MyTaskSerializer(queryset, many = True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk):
        try:
            queryset = MyTask.objects.get(pk = pk)
        except List.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = MyTaskSerializer(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk):
        id = pk
        task = MyTask.objects.get(pk=id)
        serializer = MyTaskSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        try:
            obj = MyTask.objects.get(pk=pk)
            obj.delete()
            return Response(status=status.HTTP_200_OK)
        except MyTask.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
    

    def list_task(self, request, list_id):
        queryset = MyTask.objects.filter(list_id = list_id).all()
        serializer = MyTaskSerializer(queryset, many = True)
        return Response(serializer.data)





    # queryset = User.objects.all()
    # serializer_class = UserSerializer

# class ListViewSet(viewsets.ModelViewSet):
#     queryset = List.objects.all()
#     serializer_class = ListSerializer
    
# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = MyTask.objects.all()
#     serializer_class = MyTaskSerializer