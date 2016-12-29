"""Activity Configuration"""

from collections import OrderedDict as odict

ACTIVITY_CONFIG = odict([
    ('Sample', odict([
        ('sample_id', ['create', 'update', 'display']),
        ('internal_sample_id', ['create', 'display']),
        ('created_by', ['create', 'update', 'display']),
        ('notes', ['create', 'display']),
        ('creation_date', ['display']),
        ('last_updated', ['display'])
    ]))
])

#  config for Corge commented out to demonstrate that config is optional

# field configuration for WYSIWYG editor

WYSIWYG_CONFIG = {
    'Sample': ['notes']
}

# custom form registration

FORM_CONFIG = {
    'Sample': 'CustomForm'
}
