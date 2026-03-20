from __future__ import annotations

from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def health(request: HttpRequest) -> JsonResponse:
    _ = request
    return JsonResponse({"status": "ok", "service": "lti-backend"})

