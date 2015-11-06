# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import Group

# Create your models here.
class Services(models.Model):
    serviceName = models.CharField(
        blank=False,
        max_length=50
    )

    class Meta:
        db_table = "service"

class RoleMessage(models.Model):
    service = models.ForeignKey(Services, blank=False)
    role = models.ForeignKey(Group, blank=False)
    message = models.CharField(max_length=256, blank=False, default="")
