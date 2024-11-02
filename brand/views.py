from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Brand
from .serializers import BrandSerializer

class GetUserBrandsView(generics.ListAPIView):
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the brands for the logged-in user
        user = self.request.user
        return Brand.objects.filter(user=user)
