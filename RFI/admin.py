from django.contrib import admin
from .models import Post, SignUp, Contact
from .forms import SignUpForm, ContactForm

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__", "timestamp", "updated"]
	form = SignUpForm
	#class Meta:
	#	model = SignUp

class ContactAdmin(admin.ModelAdmin):
	list_display = ["__str__", "client_name", "client_address"]
	form = ContactForm


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Contact)	
admin.site.register(Post)
