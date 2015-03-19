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
#print "Sted: " + collection.getElementsByTagName('location')[2].attributes['name'].value 
#print "Fra: " + collection.getElementsByTagName('time')[4].attributes['from'].value + " til: " + collection.getElementsByTagName('time')[4].attributes['to'].value
print "Dag: " + collection.getElementsByTagName('title')[0].childNodes[0].data
    
def fetchXML(land, fylke, kommune, sted):
    #URL = urllib.urlopen("http://www.yr.no/sted/Norge/vest-agder/flekkefjord/flekkefjord/varsel.xml")
    URL = urllib.urlopen("http://www.yr.no/sted/"+land+"/"+fylke+"/"+kommune+"/"+sted+"/varsel.xml")
    DOMTree = xml.dom.minidom.parse(URL)
    collection = DOMTree.documentElement
    print "Forecast for next 24 houres"
    print "Place: " + collection.getElementsByTagName('location')[2].attributes['name'].value
    print " ---------------------------------------------------------------"
    print "From: " + collection.getElementsByTagName('time')[5].attributes['from'].value + " Til: " + collection.getElementsByTagName('time')[5].attributes['to'].value
    print "Temprature: " + collection.getElementsByTagName('time')[5].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[5].childNodes[13].attributes['unit'].value
    print "Skyes: " + collection.getElementsByTagName('time')[5].childNodes[3].attributes['name'].value
    print "Rainfall: " + collection.getElementsByTagName('time')[5].childNodes[5].attributes['value'].value + " mm"
    print "Wind: " + collection.getElementsByTagName('time')[5].childNodes[9].attributes['name'].value + ", " + collection.getElementsByTagName('time')[5].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[5].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print " ---------------------------------------------------------------"
    print "From: " + collection.getElementsByTagName('time')[6].attributes['from'].value + " Til: " + collection.getElementsByTagName('time')[6].attributes['to'].value
    print "Temprature: " + collection.getElementsByTagName('time')[6].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[6].childNodes[13].attributes['unit'].value
    print "Skyes: " + collection.getElementsByTagName('time')[6].childNodes[3].attributes['name'].value
    print "Rainfall: " + collection.getElementsByTagName('time')[6].childNodes[5].attributes['value'].value + " mm"
    print "Wind: " + collection.getElementsByTagName('time')[6].childNodes[9].attributes['name'].value +  ", " + collection.getElementsByTagName('time')[6].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[6].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print " ---------------------------------------------------------------"
    print "From: " + collection.getElementsByTagName('time')[7].attributes['from'].value + " Til: " + collection.getElementsByTagName('time')[7].attributes['to'].value
    print "Temprature: " + collection.getElementsByTagName('time')[7].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[7].childNodes[13].attributes['unit'].value
    print "Tilstand: " + collection.getElementsByTagName('time')[7].childNodes[3].attributes['name'].value
    print "Rainfall: " + collection.getElementsByTagName('time')[7].childNodes[5].attributes['value'].value + " mm"
    print "Wind: " + collection.getElementsByTagName('time')[7].childNodes[9].attributes['name'].value +  ", " + collection.getElementsByTagName('time')[7].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[7].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print " ---------------------------------------------------------------"
    print "From: " + collection.getElementsByTagName('time')[8].attributes['from'].value + " Til: " + collection.getElementsByTagName('time')[8].attributes['to'].value
    print "Temprature: " + collection.getElementsByTagName('time')[8].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[8].childNodes[13].attributes['unit'].value
    print "Tilstand: " + collection.getElementsByTagName('time')[8].childNodes[3].attributes['name'].value
    print "Rainfall: " + collection.getElementsByTagName('time')[8].childNodes[5].attributes['value'].value + " mm"
    print "Wind: " + collection.getElementsByTagName('time')[8].childNodes[9].attributes['name'].value +  ", " + collection.getElementsByTagName('time')[8].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[8].childNodes[11].attributes['mps'].value + " Meter i sekundet"

    
def tull():
    URL = urllib.urlopen("http://www.yr.no/sted/Norge/vest-agder/flekkefjord/flekkefjord/varsel.xml")
    DOMTree = xml.dom.minidom.parse(URL)
    collection = DOMTree.documentElement
    print "Forecast for next 24 houres"
    print "Place: " + collection.getElementsByTagName('location')[2].attributes['name'].value
    print " ---------------------------------------------------------------"
    print "From: " + collection.getElementsByTagName('time')[5].attributes['from'].value + " Til: " + collection.getElementsByTagName('time')[5].attributes['to'].value
    print "Temprature: " + collection.getElementsByTagName('time')[5].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[5].childNodes[13].attributes['unit'].value
    print "Skyes: " + collection.getElementsByTagName('time')[5].childNodes[3].attributes['name'].value
    print "Rainfall: " + collection.getElementsByTagName('time')[5].childNodes[5].attributes['value'].value + " mm"
    print "Wind: " + collection.getElementsByTagName('time')[5].childNodes[9].attributes['name'].value + ", " + collection.getElementsByTagName('time')[5].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[5].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print " ---------------------------------------------------------------"
    print "From: " + collection.getElementsByTagName('time')[6].attributes['from'].value + " Til: " + collection.getElementsByTagName('time')[6].attributes['to'].value
    print "Temprature: " + collection.getElementsByTagName('time')[6].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[6].childNodes[13].attributes['unit'].value
    print "Skyes: " + collection.getElementsByTagName('time')[6].childNodes[3].attributes['name'].value
    print "Rainfall: " + collection.getElementsByTagName('time')[6].childNodes[5].attributes['value'].value + " mm"
    print "Wind: " + collection.getElementsByTagName('time')[6].childNodes[9].attributes['name'].value +  ", " + collection.getElementsByTagName('time')[6].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[6].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print " ---------------------------------------------------------------"
    print "From: " + collection.getElementsByTagName('time')[7].attributes['from'].value + " Til: " + collection.getElementsByTagName('time')[7].attributes['to'].value
    print "Temprature: " + collection.getElementsByTagName('time')[7].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[7].childNodes[13].attributes['unit'].value
    print "Tilstand: " + collection.getElementsByTagName('time')[7].childNodes[3].attributes['name'].value
    print "Rainfall: " + collection.getElementsByTagName('time')[7].childNodes[5].attributes['value'].value + " mm"
    print "Wind: " + collection.getElementsByTagName('time')[7].childNodes[9].attributes['name'].value +  ", " + collection.getElementsByTagName('time')[7].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[7].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    print " ---------------------------------------------------------------"
    print "From: " + collection.getElementsByTagName('time')[8].attributes['from'].value + " Til: " + collection.getElementsByTagName('time')[8].attributes['to'].value
    print "Temprature: " + collection.getElementsByTagName('time')[8].childNodes[13].attributes['value'].value + " " + collection.getElementsByTagName('time')[8].childNodes[13].attributes['unit'].value
    print "Tilstand: " + collection.getElementsByTagName('time')[8].childNodes[3].attributes['name'].value
    print "Rainfall: " + collection.getElementsByTagName('time')[8].childNodes[5].attributes['value'].value + " mm"
    print "Wind: " + collection.getElementsByTagName('time')[8].childNodes[9].attributes['name'].value +  ", " + collection.getElementsByTagName('time')[8].childNodes[11].attributes['name'].value + " " + collection.getElementsByTagName('time')[8].childNodes[11].attributes['mps'].value + " Meter i sekundet"
    
def cancel():
    #if tkMessageBox.askokcancel("Quit", "Are you sure?"):
        root.destroy()
        
def search():    
    land = tkSimpleDialog.askstring("Vær fra Yr.no", "Skriv land\n")
    fylke = tkSimpleDialog.askstring("Vær fra Yr.no", " Skriv fylke\n")
    kommune = tkSimpleDialog.askstring("Vær fra Yr.no", "Skriv kommune\n")
    sted = tkSimpleDialog.askstring("Vær fra Yr.no", "Skriv sted\n")
    output = fetchXML(land, fylke, kommune, sted)



search = Button(app, text = "Search", command = search)
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
