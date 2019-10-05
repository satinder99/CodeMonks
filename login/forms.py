from django import forms

class DataForm(forms.Form):
    university_roll_no = forms.BooleanField(required=False)
    full_name = forms.BooleanField(required=False)
    student_mobile_no = forms.BooleanField(required=False)
    student_email = forms.BooleanField(required=False)
    gender = forms.BooleanField(required=False)
    address = forms.BooleanField(required=False)
    aggregate_sgpa = forms.BooleanField(required=False)
    aggregate_active_backlogs = forms.BooleanField(required=False)

class ConditionForm(forms.Form):

    min_sgpa = forms.CharField(widget=forms.TextInput(), required=False, label='Min. SGPA')
    max_backlogs = forms.CharField(widget=forms.TextInput(), required=False, label='Max. Backlogs')
    CHOICES = [('male', 'Male'), ('female', 'Female'), ('both', 'Both')]
    gender_select = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect({'required':'required'}), required=True, label='Gender')
    # BRANCH_CHOICES = [
    #     ('cse', 'CSE'),
    #     ('ece', 'ECE'),
    #     ('ce', 'CE'),
    #     ('pe', 'PE'),
    #     ('mba', 'MBA'),
    #     ('mca', 'MCA'),
    #     ('ee', 'EE'),
    #     ('ie', 'IE'),
    # ]
    # branch = forms.CharField(label='Select multiple branch', widget=forms.Select({'multiple':'multiple'},choices=BRANCH_CHOICES))

class SearchForm(forms.Form):
    URN = forms.CharField(widget=forms.TextInput(), required=False, label='')