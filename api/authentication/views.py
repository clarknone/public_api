from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.auth.helper.login import login_helper
from authentication.auth.serializers import serializers
from authentication.auth.services.auth import validate_user


class SignIn(APIView):
    serializer_class = serializers.LoginSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            user = validate_user(**serializer.validated_data)
            data = login_helper(data, user)
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
