# -*- coding: latin-1 -*-
#
#	Eksperimenter #1 IS-303 Våren 2015
# 	Ser på moduler urllib, json, xml.dom.minidom og datetime.datetime
# 	Utførsker JSON og XML formater fra diverse webtjenester (openweathermap.org, yr.no)
# 	Viser bruken av dict og objekter i Python
#
#   Referanser:
#			https://docs.python.org/2/library/json.html
#			https://docs.python.org/2/library/urllib.html
#			https://docs.python.org/2/library/xml.dom.html
#			http://www.tutorialspoint.com/python/python_xml_processing.htm
#
# 	Et eksempel på data i JSON format, 
#	hentet med http://api.openweathermap.org/data/2.5/weather?q=Oslo,no
#
# {"coord":{"lon":8,"lat":58.15},"sys":{"message":0.0254,"country":"NO","sunrise":1421740460,"sunset":1421767431},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"base":"cmc stations","main":{"temp":275.913,"temp_min":275.913,"temp_max":275.913,"pressure":1020.42,"sea_level":1027.96,"grnd_level":1020.42,"humidity":100},"wind":{"speed":9.31,"deg":103.5},"clouds":{"all":92},"rain":{"3h":2.5},"dt":1421751166,"id":3149318,"name":"Kristiansand","cod":200}
#
#	Du kan se på alle nøkklene med 
#		wf_owm.keys() 
#	
# 	Flere dagers varsel finnes det også:
# 		http://api.openweathermap.org/data/2.5/forecast?q=Oslo,us&mode=json
#
# 	Her er også URL-en til værdata for Oslo fra yr.no på XML format.
# 		http://www.yr.no/sted/Norge/Oslo/Oslo/Blindern/varsel_time_for_time.xml
# 		http://www.yr.no/sted/Norge/Vest-Agder/Kristiansand/Kjevik/varsel_time_for_time.xml
#
# 	Eller fra eKlima http://eklima.met.no/metdata/MetDataService?invoke=getMetData&timeserietypeID=0&format=&from=2006-01-01&to=2006-01-05&stations=18700&elements=tam&hours=&months=&username=
#
#		Parameterforklaringer:
#			http://openweathermap.org/weather-data#16days
#			http://openweathermap.org/weather-data#5days
#			http://openweathermap.org/weather-data#current
#
# 	Se http://eklima.met.no/wsKlima/start/start_no.html for mer info om web service
#
# 	Diverse hjelpefunksjoner (behandling av tid og dato):
#		http://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date-in-python
#		http://stackoverflow.com/questions/13685201/how-to-add-hours-to-current-time-in-python
#
#
#  	Installasjoner for videre eksperimentering
#		pip2.7 install freebase (fungerte både på 2.6 og 2.7)
#		pip2.7 install facebook-sdk (fungerte kun på 2.7)
#

import urllib
import json
from xml.dom.minidom import parse
import xml.dom.minidom

from datetime import datetime, timedelta


# Lager en fil-objekt basert på data fra URL-en fra en webtjeneste
f = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Oslo,no")


# Overfører data til en Python data struktur "dict" (dictionary, - en nøkkel/verdi liste)
wf_owm = json.load(f)


# Du kan liste alle nøkkler med wf_own.keys()
# Her "graver" jeg inn i "dict" samtidig som jeg omformatterer litt (ikke bra lesbarhet!)
#print (datetime.fromtimestamp(wf_owm['dt'])+timedelta(hours=1)).strftime('%d-%m-%Y %H:%M:%S')
#print wf_owm['wind']['speed']
#print wf_owm['wind']['deg']


# Lager en ny fil-objekt basert på data fra yr.no
fxml = urllib.urlopen("http://www.yr.no/sted/Norge/Oslo/Oslo/Blindern/varsel_time_for_time.xml")
tull = urllib.urlopen("http://www.yr.no/sted/Norge/vest-agder/flekkefjord/flekkefjord/varsel.xml")

# Lager et objekt i Python (xml module er objektorientert og er mer 
# avansert i forhold til JSON, 
# se https://docs.python.org/2/library/xml.dom.html)
#DOMTree = xml.dom.minidom.parse(fxml)
DOMTree = xml.dom.minidom.parse(tull)

# Så "graver" vi inn i objekt-strukturen til DOMTree dokument-objektet (som i JavaScript)
collection = DOMTree.documentElement
#forecast = DOMTree.documentElement
#
# 	Her er et eksempel på en løkke for å liste ut alle barne-noder under time elementet
# 	Jeg har kommentert den ut siden den tar litt plass, men hvis koden under ikke
# 	fungerer, bør du prøve denne
#
#for cn in collection.getElementsByTagName('time')[20].childNodes:
#	print cn.nodeName


# Så "graver" vi dypere ... Ikke bra praksis med hardkoding av indekser
# Kan du finne en løsning for å unngå det?
#Dette er for Oslo gjennom yr.
#print collection.getElementsByTagName('time')[20].attributes['from'].value
#print collection.getElementsByTagName('time')[20].childNodes[11].attributes['mps'].value
# Elementet windDirection har attributter deg, code og name


#Vær fra varsel og ikke time for time
print "From: " + collection.getElementsByTagName('time')[1].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[1].attributes['to'].value
print "Vindretning: " + collection.getElementsByTagName('time')[1].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[1].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['mps'].value + " Meter i sekundet"
print "Tilstand: " + collection.getElementsByTagName('time')[1].childNodes[3].attributes['name'].value
print "Temperatur: " + collection.getElementsByTagName('time')[1].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[1].childNodes[13].attributes['unit'].value
print "Nedbor: " + collection.getElementsByTagName('time')[1].childNodes[5].attributes['value'].value + " mm"
print "---------------------------------------------------------------------------"
print "From: " + collection.getElementsByTagName('time')[19].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[19].attributes['to'].value
print "Vindretning: " + collection.getElementsByTagName('time')[19].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['mps'].value + " Meter i sekundet"
print "Tilstand: " + collection.getElementsByTagName('time')[19].childNodes[3].attributes['name'].value
print "Temperatur: " + collection.getElementsByTagName('time')[19].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[18].childNodes[13].attributes['unit'].value
print "Nedbor: " + collection.getElementsByTagName('time')[19].childNodes[5].attributes['value'].value + " mm"
print "---------------------------------------------------------------------------"
print "From: " + collection.getElementsByTagName('time')[20].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[20].attributes['to'].value
print "Vindretning: " + collection.getElementsByTagName('time')[20].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['mps'].value + " Meter i sekundet"
print "Tilstand: " + collection.getElementsByTagName('time')[20].childNodes[3].attributes['name'].value
print "Temperatur: " + collection.getElementsByTagName('time')[20].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[18].childNodes[13].attributes['unit'].value
print "Nedbor: " + collection.getElementsByTagName('time')[20].childNodes[5].attributes['value'].value + " mm"
print "---------------------------------------------------------------------------"
print "From: " + collection.getElementsByTagName('time')[21].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[21].attributes['to'].value
print "Vindretning: " + collection.getElementsByTagName('time')[21].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['mps'].value + " Meter i sekundet"
print "Tilstand: " + collection.getElementsByTagName('time')[21].childNodes[3].attributes['name'].value
print "Temperatur: " + collection.getElementsByTagName('time')[21].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[18].childNodes[13].attributes['unit'].value
print "Nedbor: " + collection.getElementsByTagName('time')[21].childNodes[5].attributes['value'].value + " mm"
print "---------------------------------------------------------------------------"

# WindDirection er 9, Windspeed er 11, symbol er 3, pressure er 15, temprature er 13, precipitation er 5

"""
print " Her er Været fra yr.no"
print collection.getElementsByTagName('time')[20].attributes['from'].value
print "Vindretning: " + collection.getElementsByTagName('time')[20].childNodes[9].attributes['name'].value 
print collection.getElementsByTagName('time')[20].childNodes[9].attributes['deg'].value + " Retningsgrader"
print "Tilstand: " + collection.getElementsByTagName('time')[20].childNodes[3].attributes['name'].value
print "Vindstyrke: " + collection.getElementsByTagName('time')[20].childNodes[11].attributes['mps'].value + " mps"
"""
"""
print " Her er Været fra yr.no"
print collection.getElementsByTagName('location')[0]
print collection.getElementsByTagName('time')[15].attributes['from'].value
print "Vindretning: " + collection.getElementsByTagName('time')[20].childNodes[9].attributes['name'].value 
print collection.getElementsByTagName('time')[15].childNodes[9].attributes['deg'].value + " Retningsgrader"
print "Tilstand: " + collection.getElementsByTagName('time')[15].childNodes[3].attributes['name'].value
print "Vindstyrke: " + collection.getElementsByTagName('time')[15].childNodes[11].attributes['mps'].value + " mps"
"""
#print forecast.getElementsByTagName('time')[20].attributes['from'].value
#print forecast.getElementsByTagName('time')[20].childNodes[11].attributes['mps'].value
#print forecast.getElementsByTagName('time')[20].childNodes[9].attributes['deg'].value
#print forecast.getElementsByTagName('location')[0].childNodes[0].attributes['name'].value


#print collection.getElementsByTagName('time')[20].attributes['from'].value

#
#	Du kan prøve å finne værprognosene fra de samme tidspunktene fre openweathermap.org
#	og yr.no og sammenligne de forskjellige prognosedata. 
#	En bra øvelse i å forstå hvordan arbeid med XML og JSON formater foregår. 
#	
#	Reflekter om fordeler/ulemper angående JSON og XML :)
#

