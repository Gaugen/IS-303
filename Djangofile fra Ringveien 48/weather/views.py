from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from weather.models import Weather
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

#def index(request):
  #  return HttpResponse("Hallo di fitta, detta fonke jo!")

class IndexView(generic.ListView):
    template_name = 'weather/index.html'
    context_object_name = 'test'

#def weather(request, weather):
 #   response = "This is the weather for Flekkefjord now %s."
  #  return HttpResponse(response % weather)
