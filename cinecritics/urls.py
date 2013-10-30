from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
      url(r'^$','Commentaires.views.home',name='home'),
     # url(r'^base/$','Commentaires.views.base', name='base'),
      url(r'^deconnexion/$','Commentaires.views.deconnexion',name='deconnexion'),
      url(r'^signup/$','Commentaires.views.signup'),
      url(r'^movies/$','Commentaires.views.movies',name='movies'),
      url(r'^movies/(?P<id>\d+)$','Commentaires.views.detail_movie'),       
      url(r'^movies/(?P<id>\d+)/comments/$','Commentaires.views.comment_movie'),
      url(r'^tv-series/(?P<id>\d+)/comments/$','Commentaires.views.comment_serie'),
      url(r'^tv-series/$','Commentaires.views.serie'),
      url(r'^tv-series/(?P<id>\d+)$','Commentaires.views.detail_serie'),

    # Examples:
    # url(r'^$', 'cinecritics.views.home', name='home'),
    # url(r'^cinecritics/', include('cinecritics.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      #url(r'^comments/', include('comments.urls')),	
)
