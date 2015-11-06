# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.contrib.admin.utils import flatten_fieldsets
from django.contrib.auth.models import Group

from models import Services, RoleMessage

# Register your models here.
class ServicesForm(forms.ModelForm):

    role = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(ServicesForm, self).__init__(*args, **kwargs)
        try:
            for elem in Group.objects.all():
                i = elem.pk
                service = kwargs['instance']
                group = elem
                if RoleMessage.objects.filter(service=service, role=group).count() > 0:
                    default = RoleMessage.objects.get(service=service, role=group).message
                else:
                    default = ""
                self.fields[elem.name+'_message'] = forms.CharField(widget=forms.Textarea(attrs={'class': str(i)+'_message'}), initial=default, required=False)

        except:
            pass

    def save(self, commit=True):# *args, **kwargs):
        res = super(ServicesForm, self).save(commit=False)#*args, **kwargs)

        if self.instance.pk != None:

            service = self.instance
            for elem in Group.objects.all():
                message = self.cleaned_data[elem.name+'_message']
                if RoleMessage.objects.filter(service=service, role=elem).count() > 0:
                    rm = RoleMessage.objects.get(service=service, role=elem)
                    rm.message = message
                    rm.save()
                else:
                    rm = RoleMessage(service=service, role=elem, message=message)
                    rm.save()

        return res

    class Meta:
        model = Services
        fields = '__all__'

class ServicesAdmin(admin.ModelAdmin):
    form = ServicesForm

    list_display = (
        'serviceName',
    )

    fieldsets = (
        (None, {
            'fields': (
                'serviceName',
            ),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        kwargs['fields'] = flatten_fieldsets(self.declared_fieldsets)
        return super(ServicesAdmin, self).get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(ServicesAdmin, self).get_fieldsets(request, obj)
        newfieldsets = list(fieldsets)
        fields = ['role']
        if obj != None:
            for elem in Group.objects.all():
                fields.append(elem.name+'_message')
            newfieldsets.append(['Custom Message', {'fields': fields}])
        return newfieldsets

    class Media:
        js = ("js/jquery-1.11.3.min.js", "js/box.js")



admin.site.register(Services, ServicesAdmin)