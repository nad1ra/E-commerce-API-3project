from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Review
from .serializers import ReviewSerializer
from products.models import Product


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        product_id = self.kwargs.get("pk")
        user = request.user

        if Review.objects.filter(product_id=product_id, user=user).exists():
            return Response({
                "success": False,
                "message": "You have already submitted a review for this product."
            }, status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.get(id=product_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, product=product)

        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
