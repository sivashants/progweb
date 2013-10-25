from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
      url(r'^$','Commentaires.views.home'),
      url(r'^connexion/$','Commentaires.views.connexion', name='connexion'),  	
      url(r'^signin','Commentaires.views.logedin'),
      url(r'^deconnexion/$','Commentaires.views.deconnexion',name='deconnexion'),
    # Examples:
    # url(r'^$', 'cinecritics.views.home', name='home'),
    # url(r'^cinecritics/', include('cinecritics.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      #url(r'^comments/', include('comments.urls')),	
)
