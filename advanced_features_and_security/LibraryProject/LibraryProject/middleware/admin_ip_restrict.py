# LibraryProject/middleware/admin_ip_restrict.py
from django.conf import settings
from django.http import HttpResponseForbidden

class AdminIPRestrictMiddleware:
    """Return 403 if accessing admin from non-whitelisted IPs."""
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed = getattr(settings, "ADMIN_ALLOWED_IPS", [])

    def __call__(self, request):
        if request.path.startswith(settings.ADMIN_URL_PATH):
            # Obtain client IP (may need to adapt if behind proxy)
            ip = request.META.get("REMOTE_ADDR")
            if self.allowed and ip not in self.allowed:
                return HttpResponseForbidden("Forbidden")
        return self.get_response(request)
