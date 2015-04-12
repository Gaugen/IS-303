from django.conf.urls import patterns, url
from weather import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<Yr>\d+)/results/$', views.weather, name='yr'),
    
)
