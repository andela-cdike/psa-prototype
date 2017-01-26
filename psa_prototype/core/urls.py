from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^$', views.HomePageView.as_view(), name='home'),
]
