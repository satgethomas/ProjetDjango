from django import forms


from django.forms.models import ModelForm
from .models import Student, Presence


class StudentForm(ModelForm):
    class Meta:
        model = Student

        fields = (
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "phone",
            "comments",
            "cursus",
        )

class PresenceForm(ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.order_by('last_name'))

    class Meta:
            model = Presence

            fields = (
                'date',
                "isMissing",
                "reason",
                'student',
            )


class SectionForm(forms.Form):
    date = forms.DateInput()

    choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
    )
