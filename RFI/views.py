from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .models import Post
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
	return render(request, "RFI/email.html", context)

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'RFI/post_list.html', {'posts': posts})


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		subject = "site contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'yourotheremail@email.com']
		contact_message = "%s: %s via %s"%(form_full_name, 
			form_message, 
			form_email)

		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email, 
			fail_silently=False)

	context = {
		"form" : form,
	}
	return render(request, "RFI/forms.html", context)
