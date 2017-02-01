from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Quote, Customer


class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email')


class QuoteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='quote_id')

    class Meta:
        model = Quote
        fields = ('id', 'zipcode')


class CustomerSerializer(serializers.ModelSerializer):
    """docstring for CustomerSerializer"""
    user = UserSerializer(read_only=True)
    quote = QuoteSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ('user', 'quote')
