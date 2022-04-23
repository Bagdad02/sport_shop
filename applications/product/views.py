from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from applications.product.models import Product, Category, Rating, Like
from applications.product.serializers import CategorySerializers, ProductSerializer, RatingSerializers


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 50


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['id', 'price']
    search_fields = ['title', 'status']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'rating':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['POST'], detail=True)
    def rating(self, request, pk):  # http://localhost:8000/product/id_product/rating/
        serializer = RatingSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            obj = Rating.objects.get(product=self.get_object(), owner=request.user)
            obj.rating = request.data['rating']
        except Rating.DoesNotExist:
            obj = Rating(owner=request.user, product=self.get_object(), rating=request.data['rating'])
        obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=True)
    def like(self, request, pk):
        product = self.get_object
        like_obj, _ = Like.objects.get_or_create(product=product, owner=request.user)

        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'liked'
        if not like_obj.like:
            status = 'unlike'
        return Response({'status': status})


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]


class CategoryDeleteUpdateRetriveView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]







