from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Category, Product, Image, Comments
from .serializers import CategorySerializer, ProductSerializer, ImageSerializer, CommentModelSerializer
from .permissions import GetOrPostPermission , WorkingDays ,DeleteTwoMinutesPermission



class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Override this method to handle the creation of the category"""
        serializer.save()

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        """Override this method to handle the deletion of a category"""
        instance.delete()

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Override this method to handle the creation of a product"""
        product = serializer.save()

        # Handle image creation if it's part of the request
        image_file = self.request.FILES.get('image')
        if image_file:
            Image.objects.create(
                product=product,
                image=image_file,
                is_primary=True
            )

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        """Override this method to handle the update of a product"""
        product = serializer.save()

        image_file = self.request.FILES.get('image')
        if image_file:
            product.images.filter(is_primary=True).delete()
            Image.objects.create(
                product=product,
                image=image_file,
                is_primary=True
            )

    def perform_destroy(self, instance):
        """Override this method to handle the deletion of a product"""
        instance.delete()

class ImageView(generics.RetrieveAPIView):
    queryset = Image.objects.all()

    def get(self, request, pk, *args, **kwargs):
        image = get_object_or_404(Image, pk=pk)
        image_url = request.build_absolute_uri(image.image.url)
        return Response({'image_url': image_url}, content_type='image/jpeg')

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentModelSerializer
    queryset = Comments.objects.all()
