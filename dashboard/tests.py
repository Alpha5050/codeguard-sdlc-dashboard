
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import SecurityFinding


User = get_user_model()


class SecurityFindingTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        self.finding = SecurityFinding.objects.create(
            title="Weak Password Protection",
            description="Users are using weak passwords.",
            category="endpoint_ide",
            severity="High",
            status="Open",
            created_by=self.user
        )

    def test_security_finding_is_created(self):
        self.assertEqual(
            SecurityFinding.objects.count(), 1
        )
        self.assertEqual(
            self.finding.title, "Weak Password Protection"
        )

    def test_dashboard_requires_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_can_view_dashboard(self):
        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_finding_appears_on_dashboard(self):
        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        response = self.client.get("/")
        self.assertContains(response, "Weak Password Protection")
