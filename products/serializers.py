from rest_framework import serializers

from . models import Product

class PrdoductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
        "id",
        "title",
        "content",
        "price",
        "sale_price",
        "general_sales_tax",
        "discount",
        "total_records",
    ]
    
    def get_discount(self, obj):
        if not hasattr(obj,'id'):
            return None  
             
        if not isinstance(obj, Product):
            return None
        
        return obj.get_discount()
       
    
        
    

    
