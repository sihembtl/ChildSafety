from Front.permissions import FullDjangoModelPermissions, IsAdminOrReadOnly, ViewCustomerHistoryPermission
from Front.pagination import DefaultPagination
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from .filters import ChildFilter
from .models import Child, Parent, Activity, Schedule, App, Devices
from .serializers import ChildSerializer, ParentSerializer, ActivitySerializer, ScheduleSerializer, AppSerializer, DevicesSerializer


class ChildViewSet(ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ChildFilter
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['name']
    ordering_fields = ['name']

    def get_serializer_context(self):
        return {'request': self.request}

class ParentViewSet(ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ChildSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ChildFilter
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['name']
    ordering_fields = ['name']

    def get_serializer_context(self):
        return {'request': self.request}


class DeviceViewSet(ModelViewSet):
    serializer_class = DevicesSerializer

class ActivityViewSet(ModelViewSet):
    serializer_class = DevicesSerializer

class ScheduleViewSet(ModelViewSet):
    serializer_class = DevicesSerializer

class AppViewSet(ModelViewSet):
    serializer_class = AppSerializer