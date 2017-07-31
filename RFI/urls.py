from django.conf.urls import url
from . import views

urlpatterns= [
	url(r'^$', views.email, name='email'),
	url(r'^test/$', views.testemail, name='test'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^post_list/$', views.post_list, name='post_list'),
]
