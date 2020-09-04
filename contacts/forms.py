from django import forms
from .models import CompanyContact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Name *'
        }
    ))
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Email *'
        }
    ))
    phone_number = forms.IntegerField(label="", widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Phone Number *'
        }
    ))
    message = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control-label',
            'placeholder': '  Your Message...'
        }
    ))


class CompanyContactForm(forms.ModelForm):
    class Meta:
        model = CompanyContact 
        fields = '__all__'
        widgets = {
            'company_email': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Enter Company Email'
                }
            ),
            'company_phone': forms.NumberInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Enter Company Phone Number'
                }
            ),
            'company_location': forms.TextInput(
                attrs= {
                    'class': 'input',
                    'placeholder': 'Enter Company Offices Location'
                }
            )
        }