from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Event(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        CANCELLED = "cancelled", "Cancelled"

    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    starts_at = models.DateTimeField()
    location = models.CharField(max_length=255)
    presenter = models.CharField(max_length=200)
    participant_limit = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ["starts_at", "pk"]
        constraints = [
            models.CheckConstraint(condition=models.Q(participant_limit__gte=1), name="event_positive_limit"),
            models.CheckConstraint(condition=models.Q(status__in=["draft", "published", "cancelled"]), name="event_valid_status"),
        ]
        permissions = [("publish_event", "Can publish own events"), ("cancel_event", "Can cancel own events")]

    def __str__(self):
        return self.title


class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deliver_at = models.DateTimeField()
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-deliver_at", "-pk"]
        indexes = [models.Index(fields=["recipient", "deliver_at"], name="notification_recipient_due")]
