# -*- coding: latin-1 -*-
#
#	Eksperimenter #1 IS-303 V�ren 2015
# 	Ser p� moduler urllib, json, xml.dom.minidom og datetime.datetime
# 	Utf�rsker JSON og XML formater fra diverse webtjenester (openweathermap.org, yr.no)
# 	Viser bruken av dict og objekter i Python
#
#   Referanser:
#			https://docs.python.org/2/library/json.html
#			https://docs.python.org/2/library/urllib.html
#			https://docs.python.org/2/library/xml.dom.html
#			http://www.tutorialspoint.com/python/python_xml_processing.htm
#
# 	Et eksempel p� data i JSON format, 
#	hentet med http://api.openweathermap.org/data/2.5/weather?q=Oslo,no
#
# {"coord":{"lon":8,"lat":58.15},"sys":{"message":0.0254,"country":"NO","sunrise":1421740460,"sunset":1421767431},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"base":"cmc stations","main":{"temp":275.913,"temp_min":275.913,"temp_max":275.913,"pressure":1020.42,"sea_level":1027.96,"grnd_level":1020.42,"humidity":100},"wind":{"speed":9.31,"deg":103.5},"clouds":{"all":92},"rain":{"3h":2.5},"dt":1421751166,"id":3149318,"name":"Kristiansand","cod":200}
#
#	Du kan se p� alle n�kklene med 
#		wf_owm.keys() 
#	
# 	Flere dagers varsel finnes det ogs�:
# 		http://api.openweathermap.org/data/2.5/forecast?q=Oslo,us&mode=json
#
# 	Her er ogs� URL-en til v�rdata for Oslo fra yr.no p� XML format.
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
#		pip2.7 install freebase (fungerte b�de p� 2.6 og 2.7)
#		pip2.7 install facebook-sdk (fungerte kun p� 2.7)
#

import urllib
import json
from xml.dom.minidom import parse
import xml.dom.minidom

from datetime import datetime, timedelta


# Lager en fil-objekt basert p� data fra URL-en fra en webtjeneste
f = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Oslo,no")


# Overf�rer data til en Python data struktur "dict" (dictionary, - en n�kkel/verdi liste)
wf_owm = json.load(f)


# Du kan liste alle n�kkler med wf_own.keys()
# Her "graver" jeg inn i "dict" samtidig som jeg omformatterer litt (ikke bra lesbarhet!)
print (datetime.fromtimestamp(wf_owm['dt'])+timedelta(hours=1)).strftime('%d-%m-%Y %H:%M:%S')
print wf_owm['wind']['speed']
print wf_owm['wind']['deg']


# Lager en ny fil-objekt basert p� data fra yr.no
fxml = urllib.urlopen("http://www.yr.no/sted/Norge/Oslo/Oslo/Blindern/varsel_time_for_time.xml")
lxml = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=London&mode=xml")

# Lager et objekt i Python (xml module er objektorientert og er mer 
# avansert i forhold til JSON, 
# se https://docs.python.org/2/library/xml.dom.html)
DOMTree = xml.dom.minidom.parse(fxml)
DOMTree = xml.dom.minidom.parse(lxml)

# S� "graver" vi inn i objekt-strukturen til DOMTree dokument-objektet (som i JavaScript)
collection = DOMTree.documentElement

#
# 	Her er et eksempel p� en l�kke for � liste ut alle barne-noder under time elementet
# 	Jeg har kommentert den ut siden den tar litt plass, men hvis koden under ikke
# 	fungerer, b�r du pr�ve denne
#
#for cn in collection.getElementsByTagName('time')[20].childNodes:
#	print cn.nodeName


# S� "graver" vi dypere ... Ikke bra praksis med hardkoding av indekser
# Kan du finne en l�sning for � unng� det?
#Dette er for Oslo gjennom yr.
print collection.getElementsByTagName('time')[20].attributes['from'].value
print collection.getElementsByTagName('time')[20].childNodes[11].attributes['mps'].value
# Elementet windDirection har attributter deg, code og name
print collection.getElementsByTagName('time')[20].childNodes[9].attributes['deg'].value

#Dette er for London gjennom openweather
#print collection.getElementsByTagName('time')[20].attributes['from'].value

#
#	Du kan pr�ve � finne v�rprognosene fra de samme tidspunktene fre openweathermap.org
#	og yr.no og sammenligne de forskjellige prognosedata. 
#	En bra �velse i � forst� hvordan arbeid med XML og JSON formater foreg�r. 
#	
#	Reflekter om fordeler/ulemper ang�ende JSON og XML :)
#
