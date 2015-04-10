# -*- coding: cp1252 -*-
from django.db import models
import json, urllib, urllib2
from xml.dom.minidom import parse
import xml.dom.minidom
from datetime import datetime, timedelta
     
class Owm(models.Model):
    OWM = "http://api.openweathermap.org/data/2.5/weather?q=flekkefjord"
    req = urllib2.Request(OWM)
    response=urllib2.urlopen(req)

    output = response.read()
    data = json.loads(output)
    print("Results", "Location: " + str(data['name']) +
                              "\n\nCountry: "+ str(data['sys']['country']) +
                               "\n\nLongitude: " +str(data['coord']['lon']) +
                               "\n\nTemperature: "+str(data['main']['temp']-273.15) +" C"+
                               "\n\nHumidity: " + str(data['main']['humidity']) + " %"+
                               "\n\nPressure: " + str(data['main']['pressure']) + " hPa"+
                               "\n\nWind Speed: " + str(data['wind']['speed']) + " mps" +
                               "\n\nWeather Description: " + str(data['weather'][0]['description']))



class Yr(models.Model):
    YR = urllib.urlopen("http://www.yr.no/sted/Norge/Vest-Agder/Flekkefjord/Flekkefjord/varsel_time_for_time.xml")
    DOMTree = xml.dom.minidom.parse(YR)
    collection = DOMTree.documentElement

    #Vær fra varsel og ikke time for time
    print "---------------------------------------------------------------------------"
    print "From: " + collection.getElementsByTagName('time')[5].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[5].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[5].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[5].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[5].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[5].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[5].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[5].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[5].childNodes[5].attributes['value'].value + " mm"

