from django import forms

class SummaryForm(forms.Form):
    topic = forms.CharField(label='Topic', max_length=200, required=True)
    specific_aspect = forms.CharField(label='Specific Aspect', max_length=200, required=False)
    summary_length = forms.ChoiceField(choices=[('short', 'Short'), ('medium', 'Medium'), ('detailed', 'Detailed')], required=True)
    tone = forms.ChoiceField(choices=[('formal', 'Formal'), ('casual', 'Casual'), ('academic', 'Academic')], required=True)
