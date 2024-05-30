from django.db import models
from django.core.validators import MinLengthValidator
import datetime


# Create your models here.
class Announcement(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "El título debe ser de más de dos caracteres")],
    )
    body = models.TextField()
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def was_edited(self):
        # 5 minute window to edit without it counting
        return self.created_at < (self.updated_at - datetime.timedelta(minutes=5))

    class Meta:
        verbose_name = "Anuncio"
        verbose_name_plural = "Anuncios"

    def __str__(self) -> str:
        return self.title


class Content(models.Model):
    CONTENT_TYPES = [("PR", "Presentación"), ("MA", "Material adicional"), ("SR", "Serie")]
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "El nombre debe ser de más de dos caracteres")],
    )
    url = models.URLField()
    type = models.CharField(choices=CONTENT_TYPES, max_length=30, default="MA")
    archived = models.BooleanField(default=False)
    order = models.IntegerField()

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural = "Contenidos"

    def __str__(self) -> str:
        return self.name
