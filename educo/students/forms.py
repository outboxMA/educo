from django import forms
from crispy_forms.layout import Layout, Div, Submit, Row, Column
from crispy_forms.helper import FormHelper
from .models import Student, Enrollment
from courses.models import Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'first_name_in_arabic', 'last_name_in_arabic',
            'id_card_number', 'email', 'phone', 'address',
            'parent_name', 'relationship', 'parent_email', 'parent_phone'
        ]
        widgets = {
            'first_name_in_arabic': forms.TextInput(attrs={'dir': 'rtl'}),
            'last_name_in_arabic': forms.TextInput(attrs={'dir': 'rtl'}),
        }

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if Student.objects.filter(email=email).exists():
    #         raise forms.ValidationError("A student with this email already exists.")
    #     return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Student.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A student with this phone number already exists.")
        return phone
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'space-y-4'
        
        # Set up custom layout for crispy form
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class="form-group col-md-6 mb-0"),
                Column('last_name', css_class="form-group col-md-6 mb-0"),
                css_class="form-row"
            ),
            Row(
                Column('first_name_in_arabic', css_class="form-group col-md-6 mb-0"),
                Column('last_name_in_arabic', css_class="form-group col-md-6 mb-0"),
                css_class="form-row"
            ),
            'id_card_number',
             Row(
                Column('email', css_class="form-group col-md-6 mb-0"),
                Column('phone', css_class="form-group col-md-6 mb-0"),
                css_class="form-row"
            ),
            
            'address',
            Row(
                Column('parent_phone', css_class="form-group col-md-6 mb-0"),
                Column('parent_email', css_class="form-group col-md-6 mb-0"),
                css_class="form-row"
            ),
            Row(
                Column('parent_name', css_class="form-group col-md-6 mb-0"),
                Column('relationship', css_class="form-group col-md-6 mb-0"),
                css_class="form-row"
            ),
            Submit('submit', 'Save Student', css_class='btn btn-primary w-full mt-4')
        )

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'total_fee', 'amount_paid', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()  # Limit courses to existing ones

    def clean_amount_paid(self):
        amount_paid = self.cleaned_data.get('amount_paid')
        total_fee = self.cleaned_data.get('total_fee')
        if amount_paid > total_fee:
            raise forms.ValidationError("Amount paid cannot exceed the total fee.")
        return amount_paid

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status == 'Completed' and self.cleaned_data.get('amount_paid') < self.cleaned_data.get('total_fee'):
            raise forms.ValidationError("A completed course must have the full amount paid.")
        return status
