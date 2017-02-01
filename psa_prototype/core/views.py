from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Customer, Quote
from core.serializers import CustomerSerializer, QuoteSerializer
from psa_prototype.settings import (SOCIAL_AUTH_FACEBOOK_KEY)


class HomePageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'core/home.html', {})


class LoginView(View):
    def get(self, request):
        request.path = request.GET.get('next')
        context = {'FACEBOOK_APP_ID': SOCIAL_AUTH_FACEBOOK_KEY}
        return render(request, 'core/login.html', context)


class SocialLoginSuccess(View):
    def get(self, request):
        quote_id = request.GET.get('quoteId', None)
        user_id = request.session.get('_auth_user_id')
        quote = Quote.objects.get(quote_id=quote_id)
        user = User.objects.get(pk=user_id)
        Customer.objects.create(quote=quote, user=user)

        return_url = 'http://localhost:3000/user-info'
        return redirect('{0}/?quoteId={1}'.format(return_url, quote_id))


class QuoteView(APIView):
    def post(self, request, format=None):
        zipcode = request.data.get('zipcode')
        quote = Quote.objects.create(zipcode=zipcode)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, **kwargs):
        quote_id = self.kwargs.get('quote_id')
        quote = Quote.objects.get(quote_id=quote_id)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserInfo(APIView):
    def get(self, request, **kwargs):
        quote_id = self.kwargs.get('quote_id')
        customer = Customer.objects.get(quote=quote_id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
