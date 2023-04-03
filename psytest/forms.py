from django import forms
from .models import Question

class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for question in questions:
            self.fields[str(question.id)] = forms.ChoiceField(
                choices=[(k, v) for k, v in question.options.items()],
                widget=forms.RadioSelect,
                label=question.text
            )