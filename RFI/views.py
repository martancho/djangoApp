from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.template import Context 
from django.views import generic
from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import Post, Contact
from .forms import SignUpForm, ContactForm

# Create your views here.
def email(request):
	title = 'Welcome'

	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.full_name:
			instance.full_name = "Martin"
		instance.save()
		context={
			"title": "Thank you"
		}	
	return render(request, "RFI/RFItemplate.html", context)

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'RFI/post_list.html', {'posts': posts})


def contact(request):
	title = 'Welcome'
	form = ContactForm(request.POST or None)
	context = {
		"title" : title,
		"form" : form
	}
	if form.is_valid():
		instance = form.save(commit=False)
		form_email = form.cleaned_data.get("email")
		form_full_name = form.cleaned_data.get("client_name")
		form_client_address = form.cleaned_data.get("client_address")
		form_client_address2 = form.cleaned_data.get("client_address2")
		form_message = form.cleaned_data.get("info_requested")
		form_project_name = form.cleaned_data.get("project_name")
		form_phone_number = form.cleaned_data.get("phone_number")
		form_client = form.cleaned_data.get("client")
		subject = "Tech MD inc contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "The client %s: asked about %s via %s from %s"%(form_full_name, 
			form_message,
			form_client_address, 
			from_email)
		context={
			"title":"Thank you"
		}
		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email, 
			fail_silently=False)

		instance.save()	
			
	
	return render(request, "RFI/forms.html", context)



def testemail(request):
	subject = "I am a html email"
	to = ['martancho@gmail.com']
	from_email = settings.EMAIL_HOST_USER

	ctx = {
		'user': 'tancho',
		'purchase': 'books'
	}

	message = get_template('RFI/testemail.html').render(Context(ctx))
	msg = EmailMessage(subject, message, to=to, from_email=from_email)
	msg.content_subtype = 'html'
	msg.send()

	return HttpResponse('email sent')