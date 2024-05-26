from django.db import models
from django.core.validators import MinLengthValidator
import datetime


# Create your models here.
class Announcement(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Title must be greater than 2 characters")],
    )
    body = models.TextField()
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def was_edited(self):
        # 5 minute window to edit without it counting
        return self.created_at < (self.updated_at - datetime.timedelta(minutes=5))

    def __str__(self) -> str:
        return self.title


class Content(models.Model):
    CONTENT_TYPES = [("SL", "Slide"), ("AM", "Additional material")]
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Name must be greater than 2 characters")],
    )
    url = models.URLField()
    type = models.CharField(choices=CONTENT_TYPES, max_length=30, default="AM")
    archived = models.BooleanField(default=False)
    order = models.IntegerField()

    class Meta:
        verbose_name_plural = "Content"

    def __str__(self) -> str:
        return self.name
