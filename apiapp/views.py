from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import TaskSerializer, UpdateTaskSerializer
from rest_framework.response import Response


# Create your views here.
class TaskApi(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
              GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def post(self, request, *args, **kwargs):
        user = MyUser.objects.get(username=request.user)
        if user.roles == 'Client':
            self.create(request, *args, **kwargs)
            return Response('Task created successfully.')
        else:
            return Response('As you are not client so you can not create task.')


class UpdateTaskApi(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateTaskSerializer
    queryset = Task.objects.all()

    def patch(self, request, *args, **kwargs):
        user = MyUser.objects.get(username=request.user)
        if request.POST.get('assigned_to') and user.roles == 'Manager':
            self.partial_update(request, *args, **kwargs)
            return Response('Task assigned successfully.')
        elif request.POST.get('status') and user.roles == 'Employee':
            self.partial_update(request, *args, **kwargs)
            return Response('Task status updated successfully.')
        else:
            return Response('You can not perform this action.')

    def delete(self, request, *args, **kwargs):
        user = MyUser.objects.get(username=request.user)
        if user.roles == 'Manager':
            self.destroy(request, *args, **kwargs)
            return Response('task deleted successfully.')
        else:
            return Response('You can not perform this action.')


class LogoutAPIView(GenericAPIView):
    def post(self, request):
        try:
            print(request.data)
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            print(token_obj)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
