from django.http import JsonResponse

class CheckSecretMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'X-Secret' not in request.headers:
            return JsonResponse({"message": "X-Secret header is missing!"}, status=401)

        response = self.get_response(request)
        return response
