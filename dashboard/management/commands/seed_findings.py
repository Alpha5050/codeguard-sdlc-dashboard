
from django.core.management.base import BaseCommand

from dashboard.models import SecurityFinding


SAMPLES = [
    (
        "Hard-coded API key in repository",
        "A key was found in a committed configuration file.",
        SecurityFinding.Category.VCS,
        SecurityFinding.Severity.CRITICAL,
        SecurityFinding.Status.OPEN,
    ),
    (
        "Outdated IDE plugin on developer laptop",
        "The installed plugin version has a known security issue.",
        SecurityFinding.Category.ENDPOINT_IDE,
        SecurityFinding.Severity.LOW,
        SecurityFinding.Status.OPEN,
    ),
    (
        "Pipeline runs without dependency check",
        "The CI job installs packages without vulnerability scanning.",
        SecurityFinding.Category.CICD,
        SecurityFinding.Severity.MEDIUM,
        SecurityFinding.Status.IN_PROGRESS,
    ),
    (
        "Vulnerable package in registry",
        "A dependency has a reported security vulnerability.",
        SecurityFinding.Category.REGISTRY,
        SecurityFinding.Severity.HIGH,
        SecurityFinding.Status.IN_PROGRESS,
    ),
    (
        "Debug mode enabled in production",
        "The application exposes detailed error pages.",
        SecurityFinding.Category.PRODUCTION,
        SecurityFinding.Severity.HIGH,
        SecurityFinding.Status.RESOLVED,
    ),
    (
        "Unreviewed merge to main branch",
        "Branch protection is not properly enforced.",
        SecurityFinding.Category.VCS,
        SecurityFinding.Severity.MEDIUM,
        SecurityFinding.Status.RESOLVED,
    ),
]


class Command(BaseCommand):
    help = "Load sample security findings for development and demonstrations."

    def handle(self, *args, **options):
        created_count = 0

        for title, description, category, severity, status in SAMPLES:
            finding, created = SecurityFinding.objects.get_or_create(
                title=title,
                defaults={
                    "description": description,
                    "category": category,
                    "severity": severity,
                    "status": status,
                },
            )

            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Sample data loaded. {created_count} new findings created. "
                f"{SecurityFinding.objects.count()} findings now exist."
            )
        )
