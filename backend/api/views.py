#from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import PrdoductSerializer

@api_view(["POST"])
def api_home(request , *args, **kwargs):  
    """"dfr api view"""
    #instance  = Product.objects.all().order_by("?").first()

    serializer = PrdoductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #data = serializer.save()
        #data = serializer.data
        return Response(serializer.data)
    return Response({"Message: ":"Invalid data"})



