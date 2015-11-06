# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.core import serializers

import json

# Create your views here.
def getGroups(request):
    groups = list(Group.objects.all().values_list('name', flat=True))
    return HttpResponse(json.dumps(groups), content_type='application/json')