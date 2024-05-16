from rest_framework import serializers
from rest_framework import serializers
from .models import Category, Product, Stock, Transaction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source='product.name', read_only=True)
    unit_price = serializers.DecimalField(source='product.unit_price', max_digits=10, decimal_places=2, read_only=True)
    category_name = serializers.CharField(source='product.category.name', read_only=True)

    class Meta:
        model = Stock
        fields = ['name', 'unit_price', 'category_name', 'quantity']

class TransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'
