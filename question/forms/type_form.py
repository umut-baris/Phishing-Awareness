from django import forms

#qtypes = (("website", "website"), ("email", "email"))

class QuestionType(forms.Form):
    website = forms.MultipleChoiceField(
        widget=forms.CheckboxInput,

        label="website"
    )
    email = forms.MultipleChoiceField(
        widget=forms.CheckboxInput,

        label="email"
    )


