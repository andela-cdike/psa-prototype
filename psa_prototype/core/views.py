from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


from psa_prototype.settings import (SOCIAL_AUTH_FACEBOOK_KEY)


class HomePageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'core/home.html', {})


class LoginView(View):
    def get(self, request):
        request.path = request.GET.get('next')
        context = {'FACEBOOK_APP_ID': SOCIAL_AUTH_FACEBOOK_KEY}
        return render(request, 'core/login.html', context)
