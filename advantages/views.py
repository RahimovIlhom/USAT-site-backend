from django.utils.translation import activate
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advantage
from .serializers import AdvantageSerializer


@api_view(['GET'])
def get_advantages_list(request):
    lang = request.headers.get('Accept-Language', 'uz')
    activate(lang)
    advantages = Advantage.active_objects.all().order_by('-created_at')

    serializer = AdvantageSerializer(advantages, many=True)

    return Response(data=serializer.data, status=200)
