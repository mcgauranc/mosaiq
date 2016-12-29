"""Template Tags"""

import itertools
from importlib import import_module
from collections import OrderedDict

from django.apps import apps

from django import template

from activflow.core.constants import REQUEST_IDENTIFIER
from activflow.core.helpers import (
    activity_config,
    wysiwyg_config
)
from activflow.core.models import Task

register = template.Library()


@register.filter(is_safe=True)
def label_with_class(value, arg):
    """Style adjustments"""
    return value.label_tag(attrs={'class': arg})


@register.assignment_tag(takes_context=True)
def activity_data(context, instance, option):
    """Returns activity data as in field/value pair"""
    app = context['app_title']
    model = type(instance)

    try:
        config = activity_config(app, model.__name__)
    except KeyError:
        fields = [field for field in (
            (field.name, field.verbose_name) for field in instance.class_meta.
            get_fields()) if field[0] not in ['id', 'task', 'task_id']]

        return {field[1]: getattr(
            instance, field[0]) for field in fields}

    def compute(configuration):
        """Compute fields for display"""
        for field_name in configuration:
            if option in configuration[field_name]:
                yield field_name

    return OrderedDict([(model().class_meta.get_field(
        field_name).verbose_name, getattr(
        instance, field_name)) for field_name in itertools.islice(
        compute(config), len(config))])


@register.assignment_tag(takes_context=True)
def wysiwyg_form_fields(context):
    """Returns activity data as in field/value pair"""
    app = context['app_title']
    model = context['entity_title']

    try:
        return wysiwyg_config(app, model)
    except (KeyError, AttributeError):
        return None


@register.simple_tag
def activity_title(ref, app):
    """Returns activity name"""
    return import_module(
        '{}.flow'.format(apps.get_app_config(app).name)
    ).FLOW[ref]['model']().title


@register.simple_tag
def activity_friendly_name(ref, app):
    """Returns activity friendly name"""
    return import_module(
        '{}.flow'.format(apps.get_app_config(app).name)
    ).FLOW[ref]['name']


@register.simple_tag
def request_instance(task_identifier):
    """Returns request instance"""
    return Task.objects.get(
        id=task_identifier
    ).request if task_identifier != REQUEST_IDENTIFIER else None


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})
