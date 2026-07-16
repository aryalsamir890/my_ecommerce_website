from django.urls import path
from . import views 
from django.urls import re_path
from allauth.account.views import (
    LoginView, LogoutView, SignupView,
    ConfirmEmailView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetFromKeyView, PasswordResetFromKeyDoneView,
    PasswordChangeView, PasswordSetView,
    EmailVerificationSentView,
    AccountInactiveView,
    EmailView,
)
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView, OAuth2CallbackView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

urlpatterns = [
    path('myapp/',views.myapp,name='myapp'),
    path('accounts/login',LoginView.as_view(),name='account_login'),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),
    path('accounts/google/login/', OAuth2LoginView.adapter_view(GoogleOAuth2Adapter), name='google_login'),
    path('accounts/google/login/callback/', OAuth2CallbackView.adapter_view(GoogleOAuth2Adapter), name='google_callback'),
    path('accounts/confirm-email/', EmailVerificationSentView.as_view(), name='account_email_verification_sent'),
    path('accounts/confirm-email/<key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('accounts/password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(), name='account_reset_password_done'),
    re_path(
            r'^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$',
            PasswordResetFromKeyView.as_view(),
            name='account_reset_password_from_key'),    
    path('accounts/password/reset/key/done/', PasswordResetFromKeyDoneView.as_view(), name='account_reset_password_from_key_done'),


]
