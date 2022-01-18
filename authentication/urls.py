from django.urls import path
from authentication.views import (
    RegisterView, VerifyEmail, LoginAPIView, PasswordTokeCheckAPIView, RequestPasswordResetEmail, SetNewPassword)

from rest_framework_simplejwt.views import (
    TokenRefreshView,)

# urlpatterns = [
#    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#    ...
# ]

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/', PasswordTokeCheckAPIView.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPassword.as_view(), name='password-reset-complete'),
]