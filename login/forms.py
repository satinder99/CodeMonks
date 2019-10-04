from django import forms

class DataForm(forms.Form):
    UNIVERSITY_ROLL_NO_ = forms.BooleanField(required=False)
    FULL_NAME_ = forms.BooleanField(required=False)
    STUDENTS_CONTACT_NO_ = forms.BooleanField(required=False)
    EMAIL_ADDRESS_ = forms.BooleanField(required=False)
    GENDER_ = forms.BooleanField(required=False)
    ADDRESS_ = forms.BooleanField(required=False)
    X_PERCENTAGE_ = forms.BooleanField(required=False)
    XII_PERCENTAGE_ = forms.BooleanField(required=False)
    Aggregate_SGPA_OBTAINED_ = forms.BooleanField(required=False)
    # Aggregate_ACTIVE_BACKLOGS = forms.BooleanField(required=False)

class ConditionForm(forms.Form):

    Aggregate_SGPA_OBTAINED = forms.CharField(widget=forms.TextInput(), required=False, label='Min. SGPA')
    XII_PERCENTAGE = forms.CharField(widget=forms.TextInput(), required=False, label='Min 12th Percentage')
    X_PERCENTAGE = forms.CharField(widget=forms.TextInput(), required=False, label='Min 10th Percentage')

    CHOICES = [('male', 'Male'), ('female', 'Female'), ('both', 'Both')]
    GENDER = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)


