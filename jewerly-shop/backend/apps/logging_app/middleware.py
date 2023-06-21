from .models import VisitLog

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Логируем только GET-запросы
        if request.method == 'GET':
            VisitLog.objects.create(
                url=request.path,
                method=request.method,
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )

        return response
