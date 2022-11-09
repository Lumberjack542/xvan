from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from .models import *
from .serializers import *
from rest_framework import generics, status
from django.db import transaction


class UserApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.select_related('transaction').all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )


class TransactionApiView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )


class UserProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            user_profile = Profile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'id': user_profile.id,
                    'cat': user_profile.cat,
                    'balance': user_profile.balance
                    #'balance': user_profile.balance,
                    }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)









