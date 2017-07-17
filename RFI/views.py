from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import SignUpForm
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
			"title: Thank you"
		}	
	return render(request, "RFI/email.html", context)

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'RFI/post_list.html', {'posts': posts})


