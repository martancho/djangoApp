from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default = timezone.now)
	published_date = models.DateTimeField(
		blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.email

class Contact(models.Model):
	project_name = models.CharField(max_length=200, null=True)
	client_name = models.CharField(max_length=200, blank=True, null=True)
	client_address = models.CharField(max_length=200, blank=True, null=True)
	client_address2 = models.CharField(max_length=200, blank=True, null=True)
	phone_number = models.CharField(max_length=200, null=True)
	client = models.CharField(max_length=250, null=True)
	today_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	rfi = models.CharField(max_length=6, null=True)
	email = models.EmailField(max_length=254, null=True)
	user = models.CharField(max_length=200, null = True)
	info_requested = models.TextField(max_length=250, null=True)
	description = models.TextField(max_length=500, null=True)
	response = models.TextField(max_length=500, null=True)
	user_signature = models.CharField(max_length=200, null=True)
	client_signature = models.CharField(max_length=200, null=True)
	user_date = models.DateTimeField(default=timezone.now)
	client_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.client_name 



