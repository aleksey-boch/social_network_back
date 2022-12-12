from django.http import Http404
from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response

from api.models import User, Profile
from api.serializer import UserSerializer, ProfileSerializer, AuthMeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ViewSet):
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfileSerializer

    def list(self, request):
        data = {
            'resultCode': 0,
            'messages': [],
            'data': None,
        }

        if request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be':
            data.update({'resultCode': -1, })
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        queryset = User.objects.first()
        serializer = AuthMeSerializer(queryset, many=False)
        data.update({'data': serializer.data, })

        return Response(data)


class AuthMeViewSet(viewsets.ViewSet):
    # queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    # serializer_class = AuthMeSerializer
    pagination_class = None

    def list(self, request):
        data = {
            'resultCode': 0,
            'messages': [],
            'data': None,
        }

        if request.headers.get('API-KEY') != '3dc40e5a-2498-4648-8754-bcdd62cbe9be':
            data.update({'resultCode': -1, })
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        queryset = User.objects.first()
        serializer = AuthMeSerializer(queryset, many=False)
        data.update({'data': serializer.data, })

        return Response(data)
