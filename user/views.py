from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import *
from .serializers import *
from rest_framework import generics, status, mixins
from django.db import transaction


class UserApiView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):

        queryset = self.queryset
        if self.action == 'list':
            queryset = Profile.objects.prefetch_related('transaction_set')
        return queryset

    def get_serializer_class(self):
        if self.action == 'update':
            self.serializer_class = ProfileUpdateSerializer
        else:
            self.serializer_class = ProfileSerializer
        return self.serializer_class


class TransactionApiView(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )











