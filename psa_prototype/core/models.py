from __future__ import unicode_literals

import uuid

from django.contrib.auth.models import User
from django.db import models


class Lead(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quote = models.ForeignKey('Quote', null=True, related_name='lead')


class Quote(models.Model):
    quote_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    zipcode = models.IntegerField()
