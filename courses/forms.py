from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required': 'Please enter your name'})
    email = forms.EmailField(error_messages={'required': 'Please enter your email'})
    age = forms.IntegerField(error_messages={'required': 'Please enter your age'})
    course = forms.CharField(error_messages={'required': 'Please enter your course'})
    batch = forms.IntegerField(min_value=1, error_messages={'required': 'Please enter a valid batch number'})
    department = forms.CharField(error_messages={'required': 'Please enter your department'})
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=16)
    re_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=16)
    textarea = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}), error_messages={'required': 'Please enter your message'})
    payment = forms.DecimalField(min_value=1000, max_value=15000, decimal_places=2, error_messages={'required': 'Please enter a valid payment amount'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password and password != re_password:
            raise forms.ValidationError("Passwords do not match")
    
