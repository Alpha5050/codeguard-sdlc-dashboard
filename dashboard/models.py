
from django.db import models
from django.conf import settings


class SecurityFinding(models.Model):

    # SDLC infrastructure categories
    class Category(models.TextChoices):
        ENDPOINT_IDE = 'endpoint_ide', 'Endpoint / IDE'
        VCS = 'vcs', 'Version Control System'
        CICD = 'cicd', 'CI/CD'
        REGISTRY = 'registry', 'Registry'
        PRODUCTION = 'production', 'Production'

    # Finding severity levels
    class Severity(models.TextChoices):
        CRITICAL = 'critical', 'Critical'
        HIGH = 'high', 'High'
        MEDIUM = 'medium', 'Medium'
        LOW = 'low', 'Low'
        INFO = 'info', 'Informational'

    # Finding progress
    class Status(models.TextChoices):
        OPEN = 'open', 'Open'
        IN_PROGRESS = 'in_progress', 'In Progress'
        RESOLVED = 'resolved', 'Resolved'
        CLOSED = 'closed', 'Closed'

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=Category.choices
    )

    severity = models.CharField(
        max_length=10,
        choices=Severity.choices,
        default=Severity.MEDIUM
    )

    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.OPEN
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_findings'
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_findings'
    )

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['category', 'severity']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title

# Create your models here.
