from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import AllowView, RequiredPermissionView

urlpatterns = [
    path("allow/", AllowView.as_view()),
    path("permission/", RequiredPermissionView.as_view()),
    path("login/", obtain_auth_token),
]
