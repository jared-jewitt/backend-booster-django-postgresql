from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from src.v1.models.user import User
from src.v1.serializers.user import UserSerializer


class RegisterAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        return Response(serializer.data)


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        existing_user = self.get_object(username=request.data["username"])
        serializer = UserSerializer(existing_user)
        return Response(serializer.data)


class ForgotPasswordAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        self.print("TODO")
