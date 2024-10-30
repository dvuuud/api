from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from .models import Banner, Product
from .serializers import BannerSerializer, ProductSerializer
# Create your views here.
class BannerAPIView(APIView):
    def get(self, request):
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)

class ProductViewSet(mixins.CreateModelMixin, 
                     mixins.RetrieveModelMixin, 
                     mixins.UpdateModelMixin, 
                     mixins.DestroyModelMixin, 
                     mixins.ListModelMixin, 
                     viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer