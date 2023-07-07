from rest_framework import status, views, permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


class AllowView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"message": "allow"}, status=status.HTTP_200_OK)


class RequiredPermissionView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({"message": "required"}, status=status.HTTP_200_OK)
