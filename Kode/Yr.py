import urllib, urllib2, Tkinter, tkSimpleDialog, tkMessageBox
from xml.dom.minidom import parse
import xml.dom.minidom
from datetime import datetime, timedelta
from Tkinter import *

root = Tk()
root.title("Weather from YR.no")
root.geometry()
app = Frame(root)
app.grid()



URL = urllib.urlopen("http://www.yr.no/sted/Norge/vest-agder/flekkefjord/flekkefjord/varsel.xml")
DOMTree = xml.dom.minidom.parse(URL)
collection = DOMTree.documentElement
print "Sted: " + collection.getElementsByTagName('location')[2].attributes['name'].value 
print "Fra: " + collection.getElementsByTagName('time')[0].attributes['from'].value + " til: " + collection.getElementsByTagName('time')[0].attributes['to'].value
print "Dag: " + collection.getElementsByTagName('title')[1].childNodes[0].data
    
def fetchXML():
    URL = urllib.urlopen("http://www.yr.no/sted/Norge/vest-agder/flekkefjord/flekkefjord/varsel.xml")
    #URL = urllib.urlopen("http://www.yr.no/sted/"+land+"/"+fylke+"/"+kommune+"/"+sted+"/varsel.xml")
    DOMTree = xml.dom.minidom.parse(URL)
    collection = DOMTree.documentElement
    """
    print "From: " + collection.getElementsByTagName('time')[1].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[1].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[1].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[1].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[1].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[1].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[1].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[1].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[1].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[2].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[2].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[2].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[2].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[2].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[2].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[2].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[2].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[2].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[3].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[3].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[3].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[3].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[3].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[3].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[3].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[3].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[3].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[4].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[4].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[4].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[4].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[4].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[4].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[4].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[4].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[4].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[5].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[5].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[5].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[5].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[5].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[5].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[5].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[5].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[5].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[6].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[6].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[6].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[6].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[6].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[6].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[6].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[6].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[6].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[7].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[7].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[7].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[7].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[7].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[7].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[7].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[7].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[7].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[8].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[8].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[8].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[8].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[8].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[8].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[8].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[8].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[8].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[9].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[9].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[9].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[9].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[9].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[9].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[9].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[9].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[9].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[10].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[10].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[10].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[10].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[10].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[10].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[10].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[10].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[10].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[11].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[1].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[11].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[11].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[11].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[11].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[11].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[1].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[11].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[12].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[12].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[12].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[12].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[12].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[12].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[12].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[12].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[12].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[13].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[13].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[13].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[13].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[13].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[13].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[13].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[13].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[13].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[14].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[14].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[14].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[14].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[14].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[14].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[14].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[14].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[14].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[15].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[15].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[15].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[15].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[15].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[15].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[15].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[15].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[15].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[16].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[16].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[16].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[16].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[16].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[16].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[16].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[16].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[16].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[17].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[17].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[17].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[17].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[17].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[17].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[17].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[17].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[17].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    
    print "From: " + collection.getElementsByTagName('time')[18].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[18].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[18].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[18].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[18].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[18].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[18].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    
    """
    print "From: " + collection.getElementsByTagName('time')[19].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[19].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[19].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[19].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[19].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[19].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[19].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[19].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[19].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[20].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[20].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[20].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[20].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[20].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[20].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[20].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[20].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[20].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[21].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[21].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[21].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[21].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[21].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[21].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[21].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[21].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[21].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[22].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[22].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[22].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[22].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[22].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[22].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[22].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[22].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[22].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[23].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[23].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[23].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[23].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[23].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[23].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[23].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[23].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[23].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[24].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[24].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[24].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[24].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[24].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[24].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[24].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[24].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[24].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[25].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[25].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[25].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[25].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[25].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[25].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[25].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[25].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[25].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[26].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[26].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[26].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[26].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[26].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[26].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[26].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[26].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[26].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[27].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[27].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[27].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[27].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[27].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[27].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[27].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[27].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[27].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
    """
    print "From: " + collection.getElementsByTagName('time')[28].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[28].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[28].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[28].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[28].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[28].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[28].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[28].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[28].childNodes[5].attributes['value'].value + " mm"
    print "---------------------------------------------------------------------------"
    """
def tull():
    URL = urllib.urlopen("http://www.yr.no/sted/Norge/vest-agder/flekkefjord/flekkefjord/varsel.xml")
   # URL = urllib.urlopen("www.yr.no/sted/"%s"/"%s"/"%s"/"%s"/varsel.xml") (land, fylke, kommune, sted)
    DOMTree = xml.dom.minidom.parse(URL)
    collection = DOMTree.documentElement
    #collection = minidom.parse(urllib.urlopen(URL).read())
    print "From: " + collection.getElementsByTagName('time')[18].attributes['from'].value + " To: " + collection.getElementsByTagName('time')[18].attributes['to'].value
    print "Vindretning: " + collection.getElementsByTagName('time')[18].childNodes[9].attributes['name'].value +  " Vindstyrke: " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[18].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print "Tilstand: " + collection.getElementsByTagName('time')[18].childNodes[3].attributes['name'].value
    print "Temperatur: " + collection.getElementsByTagName('time')[18].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[18].childNodes[13].attributes['unit'].value
    print "Nedbor: " + collection.getElementsByTagName('time')[18].childNodes[5].attributes['value'].value + " mm"
    
def cancel():
    #if tkMessageBox.askokcancel("Quit", "Are you sure?"):
        root.destroy()
        
def search():    
    land = tkSimpleDialog.askstring("Vær fra Yr.no", "Skriv land\n")
    fylke = tkSimpleDialog.askstring("Vær fra Yr.no", " Skriv fylke\n")
    kommune = tkSimpleDialog.askstring("Vær fra Yr.no", "Skriv kommune\n")
    sted = tkSimpleDialog.askstring("Vær fra Yr.no", "Skriv sted\n")
    output = fetchXML(land, fylke, kommune, sted)
    
    #tkMessageBox.showinfo(forecast.getElementByTagName('time')[20].attributes['from'].value,
     #                     forecast.getElementByTagName('time')[20].childNodes[11].attributes['mps'].value,
      #                    forecast.getElementByTagName('time')[20].childNodes[11].attributes['deg'].value)



search = Button(app, text = "Search", command = fetchXML)
search.grid(row=1, column=1)
Flekkefjord = Button(app, text = "Flekkefjord", command = tull)
Flekkefjord.grid(row=3, column=3)
cancel = Button(app, text = "Cancel", command = cancel)
cancel.grid(row=2, column=2)

root.mainloop()



"""def get_weather(land, fylke, kommune, sted):
    url = urlVarsel % land, fylke, kommune, sted
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = []
    for node in dom.getElementsByTagNameNS(urlVarsel, 'forecast'):
        forecasts.append({
            'date': node.getAttribute('date'),
            'low': node.getAttribute('low'),
            'high': node.getAttribute('high'),
            'condition': node.getAttribute('condition')
            })
    ycondition = dom.getElementsByTagNameNS(urlVarsel, 'condition')[0]
    return {
            'current_condition': ycondition.getAttribute('text'),
            'current_temp': ycondition.getAttribute('temp'),
            'forecasts': forecasts ,
            'title': dom.getElementsByTagName('title')[0].firstChild.data
            }

def main():
    a=get_weather("Norge, Vest-Agder, Flekkefjord, Flekkefjord")
    print '=================================='
    print '|',a['title'],'|'
    print '=================================='
    print '|current condition=',a['current_condition']
    print '|current temp     =',a['current_temp']
    print '=================================='
    print '|  today     =',a['forecasts'][0]['date']
    print '|  hight     =',a['forecasts'][0]['high']
    print '|  low       =',a['forecasts'][0]['low']
    print '|  condition =',a['forecasts'][0]['condition']
    print '=================================='
    print '|  tomorrow  =',a['forecasts'][1]['date']
    print '|  hight     =',a['forecasts'][1]['high']
    print '|  low       =',a['forecasts'][1]['low']
    print '|  condition =',a['forecasts'][1]['condition']
    print '=================================='

main()
"""
