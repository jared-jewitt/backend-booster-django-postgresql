from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from src.v1.views import user as user_views, post as post_views


router = routers.DefaultRouter()
router.register(r"posts", post_views.PostModelViewSet)

urlpatterns = [
    path(r"api/v1/", include(router.urls)),
    path(r"register/", user_views.RegisterAPIView.as_view()),
    path(r"login/", user_views.LoginAPIView.as_view()),
    path(r"forgot-password/", user_views.ForgotPasswordAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += [path(r"admin/", admin.site.urls)]
