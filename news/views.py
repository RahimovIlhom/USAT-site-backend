from drf_yasg import openapi
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from accounts.permissions import HasXSecretPermission
from advantages.views import headers_params
from .serializers import NewsListSerializer, NewsDetailSerializer, CategoryListWithNewsSerializer, \
    CategoryRelatedNewsListSerializer
from .models import News, ViewRecord, NewsCategory


class GetNewsListView(APIView):
    permission_classes = [HasXSecretPermission]

    @swagger_auto_schema(
        manual_parameters=headers_params,
        operation_summary='Barcha yangiliklar ro\'yxati',
        responses={200: NewsListSerializer(many=True)},
        examples={
            'application/json': {
                'X-Secret': 'YOUR_SECRET_VALUE',
                'Accept-Language': 'uz',
            },
        },
    )
    def get(self, request):
        news_all = News.active_objects.all().order_by('-created_at')[:20]

        return Response(data=NewsListSerializer(news_all, many=True, context={'request': request}).data, status=200)


class CategoryListWithNewsView(APIView):
    permission_classes = [HasXSecretPermission]
    @swagger_auto_schema(
        manual_parameters=headers_params,
        operation_summary="Barcha ruknlar va har bir rukn ichida so'nggi 4 yangilik bilan!",
        responses={200: CategoryListWithNewsSerializer(many=True)},
        examples={
            'application/json': {
                'X-Secret': 'YOUR_SECRET_VALUE',
                'Accept-Language': 'uz',
            },
        },
    )
    def get(self, request):
        categories = NewsCategory.active_objects.all()
        return Response(CategoryListWithNewsSerializer(categories, many=True, context={'request': request}).data, status=200)


path_param = openapi.Parameter(
    'slug',
    openapi.IN_PATH,
    description='Slug',
    type=openapi.TYPE_STRING
)


class CategoryRelatedNewsListView(APIView):
    permission_classes = [HasXSecretPermission]

    @swagger_auto_schema(
        manual_parameters=headers_params + [path_param],
        operation_summary="Rukn bo'yicha yangiliklar",
        responses={
            200: CategoryRelatedNewsListSerializer(many=False),
            404: openapi.Response(
                description="Aktiv rukn topilmadi",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties = {
                        'detail': openapi.Schema(type=openapi.TYPE_STRING, example='Rukn topilmadi (uz)')
                    }
                ),
            )
        }
    )
    def get(self, request, slug):
        lang = request.headers.get('Accept-Language', 'uz')
        try:
            category = NewsCategory.active_objects.get(slug=slug)
        except NewsCategory.DoesNotExist:
            resp_category_404 = {
                'uz': "Rukn topilmadi",
                'en': "Category not found",
                'ru': "Категория не найдена"
            }
            return Response({'detail': resp_category_404[lang]}, status=404)

        return Response(CategoryRelatedNewsListSerializer(category, context={'request': request}).data, status=200)


class GetDetailNewsView(APIView):
    permission_classes = [HasXSecretPermission]

    @swagger_auto_schema(
        manual_parameters=headers_params + [path_param],
        operation_summary='Yangilikni ID raqami orqali olish',
        responses={
            200: NewsDetailSerializer(many=False),
            404: openapi.Response(
                description='Yangilik topilmadi',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(type=openapi.TYPE_STRING, example='Yangilik topilmadi (uz)'),
                    },
                ),
            ),
        },
    )
    def get(self, request, slug):
        lang = request.headers.get('Accept-Language', 'uz')
        ip_address = get_client_ip(request)

        try:
            news = News.active_objects.get(slug=slug)

            if not ViewRecord.objects.filter(news=news, ip_address=ip_address).exists():
                ViewRecord.objects.create(news=news, ip_address=ip_address)

        except News.DoesNotExist:
            if lang == 'uz':
                return Response({'detail': 'Yangilik topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
            elif lang == 'ru':
                return Response({'detail': 'Новость не найдена.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'detail': 'News not found.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(data=NewsDetailSerializer(news, context={'request': request}).data, status=status.HTTP_200_OK)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
