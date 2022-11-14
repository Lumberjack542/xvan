from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    transaction_set = TransactionSerializer(many=True)
    cat = CategorySerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['balance']

