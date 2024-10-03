from django.utils.translation import activate
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advantage
from .serializers import AdvantageSerializer


headers_param = openapi.Parameter(
    'Accept-Language',
    openapi.IN_HEADER,
    type=openapi.TYPE_STRING,
    enum=['uz', 'en', 'ru'],
    required=False,
    description='Bu kalitga qiymatni headersda olishi kerak. Tilni tanlang: uz, en, ru'
)

@swagger_auto_schema(
    method='get',
    manual_parameters=[
        headers_param
    ],
    operation_summary='Barcha imtiyozlar ro\'yxati',
    responses={200: AdvantageSerializer(many=True)},
)
@api_view(['GET'])
def get_advantages_list(request):
    lang = request.headers.get('Accept-Language', 'uz')
    activate(lang)
    advantages = Advantage.active_objects.all().order_by('-created_at')

    serializer = AdvantageSerializer(advantages, many=True)

    return Response(data=serializer.data, status=200)
