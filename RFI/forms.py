from django import forms
from .models import SignUp, Contact
from django.forms.extras.widgets import SelectDateWidget
import datetime

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['client_name', 'client_address','client_address2', 'email', 'info_requested', 'phone_number', 'client',
		'project_name', 'rfi', 'user', 'description', 'response', 'user_signature', 'client_signature']
	
	project_name = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
			'placeholder': 'Project Name'
		}))
	client_name = forms.CharField(required = False, widget=forms.TextInput(
		attrs={
			'placeholder': '[Client Name]',
			'style' : 'width:100%'
		}))
	client_address = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
			'placeholder': '[Client Address 1]',
			'style' : 'width:100%',
			'required' : True,

		}))
	client_address2 = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
			'placeholder': '[Client Address 2]',
			'style' : 'width:100%',
		}))
	phone_number = forms.CharField(max_length=200, widget=forms.TextInput(
		attrs={
			'placeholder' : '[Phone Number]',
			'style' : 'width:100%'
		}))
	email = forms.EmailField(widget=forms.TextInput(
		attrs={
			'placeholder' : '[Email]',
			'style' : 'width:100%'
		}))
	today_date = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today())
	rfi = forms.CharField(widget=forms.TextInput(
		attrs={
			'style' : 'width:60%'
		}))
	user = forms.CharField(widget=forms.TextInput())
	client = forms.CharField(widget=forms.TextInput())
	info_requested = forms.CharField(widget=forms.Textarea(
		attrs={
			'class' : 'textInfo'
		}))
	description = forms.CharField(widget=forms.Textarea(
		attrs={
			'style':'width:100%'
		}))
	response = forms.CharField(widget=forms.Textarea(
		attrs={
			'style':'width:100%'
		}))
	user_signature = forms.CharField(widget=forms.TextInput())
	client_signature = forms.CharField(widget=forms.TextInput())
	user_date = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today())
	client_date = forms.DateTimeField(widget=forms.DateTimeInput(
		attrs={
			'type' : 'date'
		}))

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .edu email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name		
