from rest_framework import serializers

from .models import Category, Product, Image ,Comments

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'is_primary']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'images']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']

class CommentSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    def get_product_name(self, obj):
        return obj.product.name if hasattr(obj, 'product') and obj.product else None

    class Meta:
        model = Comment
        fields = ['id', 'message', 'user', 'product', 'created_at', 'image', 'bad_comment', 'good_comment', 'rating',
                  'product_name']
        read_only_fields = ['product_name', 'created_at']
