from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import HasXSecretPermission
from .models import Advantage
from .serializers import AdvantageSerializer


headers_params = [
    openapi.Parameter(
        'X-Secret',
        openapi.IN_HEADER,
        type=openapi.TYPE_STRING,
        required=True,
        description='X-Secret headeri autentifikatsiya uchun zarur.',
    ),
    openapi.Parameter(
        'Accept-Language',
        openapi.IN_HEADER,
        type=openapi.TYPE_STRING,
        enum=['uz', 'en', 'ru'],
        required=False,
        description='Tilni ko\'rsating. Variantlar: uz, en, ru',
    ),
]


class GetAdvantagesListView(APIView):
    permission_classes = [HasXSecretPermission]

    @swagger_auto_schema(
        manual_parameters=headers_params,
        operation_summary='Barcha imtiyozlar ro\'yxati',
        responses={200: AdvantageSerializer(many=True)},
    )
    def get(self, request):
        advantages = Advantage.active_objects.all().order_by('-created_at')

        serializer = AdvantageSerializer(advantages, many=True)

        return Response(data=serializer.data, status=200)