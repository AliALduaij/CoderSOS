from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import projectModel, requestModel
from . serializers import projectSerializer, requestSerializer, projectDetailSerializer, requestDetailSerializer, projectCreateSerializer, requestCreateSerializer, UserLoginSerializer


class projectListView(ListAPIView):
    queryset = projectModel.objects.all()
    serializer_class = projectSerializer


class projectDetailView(RetrieveAPIView):
    queryset = projectModel.objects.all()
    serializer_class = projectDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class projectCreateView(CreateAPIView):
    serializer_class = projectCreateSerializer

    def perform_create(self, serializer):
        serializer.save(coder=self.request.user)


class projectUpdateView(RetrieveUpdateAPIView):
    queryset = projectModel.objects.all()
    serializer_class = projectCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class projectDeleteView(DestroyAPIView):
    queryset = projectModel.objects.all()
    serializer_class = projectDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class requestListView(ListAPIView):
    queryset = requestModel.objects.all()
    serializer_class = requestSerializer


class requestDetailView(RetrieveAPIView):
    queryset = requestModel.objects.all()
    serializer_class = requestDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class requestCreateView(CreateAPIView):
    serializer_class = requestCreateSerializer

    def perform_create(self, serializer):
        serializer.save(coder_profile=self.request.user)


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
