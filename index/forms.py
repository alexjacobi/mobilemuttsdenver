from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email

class EmailContactForm(forms.Form):
	name = forms.CharField(
		required=True,
		label='',
		widget=forms.TextInput(attrs={'placeholder': 'Name'})
	)
	email_address = forms.EmailField(
		required=True,
		label='',
		widget=forms.TextInput(attrs={'placeholder': 'Email'})
	)
	subject = forms.CharField(
		required=True,
		label='',
		widget=forms.TextInput(attrs={'placeholder': 'Subject'})
	)
	message = forms.CharField(
		required=True,
		label='',
		widget=forms.Textarea(attrs={'placeholder': 'Message'})
	)

	def clean(self):
		cleaned_data = self.cleaned_data
		name = cleaned_data.get('name')

		if cleaned_data.get('email_address') is not None:
			email_address = cleaned_data.get('email_address').strip()

		subject = cleaned_data.get('subject')
		message = cleaned_data.get('message')

		return cleaned_data


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
    	required=True,
    	max_length=30
    )
    last_name = forms.CharField(
    	required=True,
    	max_length=30
    )
    email = forms.EmailField(
    	required=True,
    	max_length=254
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None
        }

    def clean(self):
    	cleaned_data=super(SignUpForm, self).clean()
    	username = cleaned_data.get('username')
    	if username == 'alexjacobi':
    		print('start')
    		raise forms.ValidationError('This username is already registered.')
    		print('end')

    	return cleaned_data


class RegistrationForm(forms.Form):
	name = forms.CharField(
		required=True,
		label='',
		widget=forms.TextInput(attrs={'placeholder': 'Name'})
	)

	def clean(self):
		cleaned_data = self.cleaned_data
		name = cleaned_data.get('name')

		return cleaned_data
