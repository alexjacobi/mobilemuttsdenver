from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context, loader
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from forms import EmailContactForm, SignUpForm

class HomeView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context['sign_up_form'] = SignUpForm()
		if self.request.method == 'POST':
			form = EmailContactForm(self.request.POST)
			if form.is_valid():
				try:
					send_mail(
					    form.cleaned_data['subject'],
					    form.cleaned_data['message'],
					    form.cleaned_data['email_address'],
					    ['mobilemuttsdenver@gmail.com'],
					    fail_silently=False
					)
					context['success'] = 'Thank you for emailing us! Someone will be in contact with you shortly.'
					form = EmailContactForm()
				except:
					context['error'] = ('Uh-Oh! Something went wrong. Please check your email address and try again.'
								         ' If this problem persists, contact us directly at mobilemuttsdenver@gmail.com')
			else:
				context['error'] = ('Uh-Oh! Something went wrong. Please check your email address and try again.'
								     ' If this problem persists, contact us directly at mobilemuttsdenver@gmail.com')
		else:
			form = EmailContactForm()

		context['form'] = form
		return context

	def post(self, *args, **kwargs):
		return self.get(*args, **kwargs)


class SignUpView(TemplateView):
	template_name = 'signup.html'

	def get_context_data(self, *args, **kwargs):
		context = super(SignUpView, self).get_context_data()
		context['form'] = SignUpForm(
			self.request.POST if self.request.method == 'POST' else None
		)
		print('1')
		return context

	def post(self, request):
		context = self.get_context_data()
		if self.request.method == 'POST':
			form = SignUpForm(self.request.POST)
	        if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password1')
				user = authenticate(username=username, password=raw_password)
				login(self.request, user)
				print('2')
				return redirect('')
		else:
			form = SignUpForm()

		#context['forms'] = form
		#return context
		print('3')
		return render(request, 'index.html', {'form': form})
