import urllib
import json
from xml.dom.minidom import parse
import xml.dom.minidom

from datetime import datetime, timedelta

# Lager et fil-objekt basert på data fra URL-en fra en webtjeneste
v = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Oslo,no")
f = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Flekkefjord,no")

# Overfører data til en Python data struktur "dict" (dictionary, - en nøkkel/verdi liste)
wf_owm = json.load(f)


# Du kan liste alle nøkkler med wf_owm.keys()
# Her "graver" jeg inn i "dict" samtidig som jeg omformatterer litt (ikke bra lesbarhet!)
print (datetime.fromtimestamp(wf_owm['dt'])+timedelta(hours=1)).strftime('%d-%m-%Y %H:%M:%S')
print wf_owm['wind']['speed']
print wf_owm['wind']['deg']


# Lager en ny fil-objekt basert på data fra yr.no
fxml = urllib.urlopen("http://www.yr.no/sted/Norge/Oslo/Oslo/Blindern/varsel_time_for_time.xml")
fxml = urllib.urlopen("http://www.yr.no/sted/Norge/Vest-Agder/Flekkefjord/Flekkefjord/time_for_time.html")
vxml = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=London&mode=xml")

# Lager et objekt i Python (xml module er objektorientert og er mer 
# avansert i forhold til JSON, 
# se https://docs.python.org/2/library/xml.dom.html)
DOMTree = xml.dom.minidom.parse(fxml)


# Så "graver" vi inn i objekt-strukturen til DOMTree dokument-objektet (som i JavaScript)
collection = DOMTree.documentElement

#
# 	Her er et eksempel på en løkke for å liste ut alle barne-noder under time elementet
# 	Jeg har kommentert den ut siden den tar litt plass, men hvis koden under ikke
# 	fungerer, bør du prøve denne
#
for cn in collection.getElementsByTagName('time')[20].childNodes:
	print cn.nodeName


# Så "graver" vi dypere ... Ikke bra praksis med hardkoding av indekser
# Kan du finne en løsning for å unngå det?
print collection.getElementsByTagName('time')[20].attributes['from'].value
print collection.getElementsByTagName('time')[20].childNodes[11].attributes['mps'].value
# Elementet windDirection har attributter deg, code og name
print collection.getElementsByTagName('time')[20].childNodes[9].attributes['deg'].value


#
#	Du kan prøve å finne værprognosene fra de samme tidspunktene fre openweathermap.org
#	og yr.no og sammenligne de forskjellige prognosedata. 
#	En bra øvelse i å forstå hvordan arbeid med XML og JSON formater foregår. 
#	
#	Reflekter om fordeler/ulemper angående JSON og XML :)
#
