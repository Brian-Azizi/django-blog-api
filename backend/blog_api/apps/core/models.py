from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order
        abstract = True
        ordering = ['created_at', 'updated_at']
