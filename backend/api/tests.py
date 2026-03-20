from __future__ import annotations

from django.test import Client, TestCase


class HealthEndpointTests(TestCase):
    def test_health_returns_200_and_expected_payload(self) -> None:
        client = Client()
        response = client.get("/health/")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload.get("status"), "ok")

