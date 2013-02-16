from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('blog.apps.home.views',
	url (r'^$','index', name ='vista_principal'),
	url (r'^contacto/$','contacto', name ='vista_contacto'),
	

)