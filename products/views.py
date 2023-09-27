from rest_framework import authentication,generics ,mixins , permissions
from .models import Product
from .serializers import PrdoductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPermission



class ProductListCreateAPIview(generics.ListCreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    #Custom Permissions 
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    queryset = Product.objects.all()
    serializer_class = PrdoductSerializer


def perform_create(self, serializer):
    #serializer.save(user=self.request.user)
    print(serializer.validated_data)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('title') or None 
    if content is None:
       content = title
    serializer.save(content=content)

product_List_create_view = ProductListCreateAPIview.as_view()

#Get By Id
class ProductDetailsAPIview(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdoductSerializer

product_deatail_view = ProductDetailsAPIview.as_view()

#Update 
class ProductUpdateAPIview(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdoductSerializer
    lookup_field = 'pk'
product_Update_view = ProductUpdateAPIview.as_view()


def perform_update(self,serializer):
    instance = serializer.save()
    if not instance:
        instance.contents = instance.title

#Update 
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdoductSerializer
    lookup_field = 'pk'


    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_delete_view = ProductDestroyAPIView.as_view()


# #Get All 
# class PrdouctListAPIView(generics.ListAPIView):
#     """We will not be using this View"""
#     queryset =  Product.objects.all()
#     serializer_class = PrdoductSerializer

# product_list_api_view = PrdouctListAPIView.as_view()

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    
    queryset = Product.objects.all()
    serializer_class = PrdoductSerializer
    lookup_field = "pk"

    def get(self , request , *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request , *args, **kwargs)
    

    def post(self , request , *args, **kwargs):
        return self.create(request , *args, **kwargs)  
    

    def put(self , request , *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.update(request , *args, **kwargs)  
        
    def delete(self , request ,*args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.destroy(request, *args, **kwargs) 

    
product_mixin_views = ProductMixinView.as_view()






@api_view(["GET", "POST"])
def product_alt_view(request,pk=None, *args, **kwargs):
    method = request.method 
    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product , pk=pk)
            data = PrdoductSerializer(obj, many=False).data
            return Response(data)
        
        query_set = Product.objects.all()
        data = PrdoductSerializer(query_set , many=True).data
        return Response(data)
    
    if method == 'POST':
        serializer = PrdoductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('title') or None 
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Message: ":"Invalid data"})




