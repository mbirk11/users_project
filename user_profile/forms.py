from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'age', 'phone', 'address', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['password'].required = False
            self.fields['password'].widget.attrs.update({'placeholder': 'Leave blank to keep current'})

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Age must be at least 18')
        return age    
    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = UserProfile.objects.filter(email=email)
        if self.instance and self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Email already exists')
        return email
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError('Phone must be digits')
        return phone    

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            if self.instance and self.instance.pk:
                return self.instance.password
            raise forms.ValidationError('This field is required')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        return password