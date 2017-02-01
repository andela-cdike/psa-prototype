from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^social-login-success',
        views.SocialLoginSuccess.as_view(),
        name='social_login_success'),

    # API URLs
    url(r'^zipcode/$', views.QuoteView.as_view(), name='create_quote'),
    url(r'^quote/(?P<quote_id>[\w-]+)$',
        views.QuoteView.as_view(),
        name='view_quote'),
    url(r'^user/(?P<quote_id>[\w-]+)$',
        views.UserInfo.as_view(),
        name='view_user'),
]
