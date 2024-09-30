from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    full_name = forms.CharField(
                widget = forms.TextInput(
                    attrs = {'class': 'form-control','placeholder': 'Enter Your Full Name',}
                )
    )
    email = forms.EmailField(
            widget = forms.EmailInput(
                attrs = {'class': 'form-control', 'placeholder': 'Enter Your Email'}
            )
    )
    message = forms.CharField(
            widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Message'}))
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'message')