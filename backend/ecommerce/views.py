from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def health_check(request):
    """Simple health check endpoint"""
    return JsonResponse({
        'status': 'healthy',
        'message': 'E-commerce backend is running!',
        'endpoints': {
            'admin': '/admin/',
            'api_auth': '/api/auth/',
            'api_products': '/api/products/',
            'api_cart': '/api/cart/',
            'api_orders': '/api/orders/',
            'api_payments': '/api/payments/',
        }
    })
