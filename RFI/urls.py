from django.conf.urls import url
from . import views

urlpatterns= [
	url(r'^$', views.email, name='email'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^$', views.post_list, name='post_list'),
]
