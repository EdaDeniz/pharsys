from django.forms import ModelForm
from patients.models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'dept',
            'address',
            'phone',
            'notes',
        ]
