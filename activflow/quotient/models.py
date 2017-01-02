"""Model definition for test workflow"""

import uuid

from django.contrib.auth.models import User

from django.contrib import admin
from django.db.models import (
    CharField,
    IntegerField,
    TextField)

from django.db import models

from activflow.core.models import AbstractActivity, AbstractInitialActivity
from activflow.quotient.validators import validate_initial_cap


class Sample(AbstractInitialActivity):
    """Sample representation of Foo activity"""
    sample_id = CharField("Sample Id:", max_length=200, validators=[validate_initial_cap])
    internal_sample_id = models.UUIDField(primary_key=False, default=uuid.uuid4)
    notes = TextField("Notes", blank=True)

    def queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(Sample, self).queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(owner=request.user)

    def clean(self):
        """Custom validation logic should go here"""
        pass


class DataValue(models.Model):
    """

    """
    name = CharField("Name", max_length=50)
    value = CharField("Value", max_length=50)


class StepDiagInformation(models.Model):
    qualified_step_name = CharField("QualifiedStepName", max_length=50)
    input_values = models.ForeignKey(DataValue, on_delete=models.CASCADE)
    intermediate_values = CharField("IntermediateValues", max_length=50)
    output_values = CharField("OutputValues", max_length=50)


class DiagnosticData(models.Model):
    results = models.ForeignKey(StepDiagInformation, on_delete=models.CASCADE)


class ImageAnalysisDiagnostic(AbstractActivity):
    """Sample representation of Corge activity"""
    execution_time = IntegerField("ExecutionTime")
    assay_type = CharField("Assay Type", max_length=50)
    conformant = CharField(verbose_name="Conformant", max_length=30, choices=(
        ('Y', 'Yes'), ('N', 'No')))

    # diagnostic_data = models.ForeignKey(DiagnosticData, on_delete=models.CASCADE)

    def clean(self):
        """Custom validation logic should go here"""
        pass


admin.site.register(Sample)
admin.site.register(StepDiagInformation)
admin.site.register(DataValue)
admin.site.register(ImageAnalysisDiagnostic)
