import urllib, urllib2, Tkinter, tkSimpleDialog, tkMessageBox
from xml.dom import minidom
from Tkinter import *

root = Tk()
root.title("Weather from YR.no")
root.geometry()
app = Frame(root)
app.grid()

#urlTimeForTime = 'www.yr.no/sted/%s/%s/%s/%s/varsel_time_for_time.xml'
#urlVarsel = "www.yr.no/sted/"+land+"/"+fylke+"/"+kommune+"/"+sted+"/varsel.xml"

def fetchXML(land, fylke, kommune, sted):
    URL = "www.yr.no/sted/"+land+"/"+fylke+"/"+kommune+"/"+sted+"/varsel.xml"
    DOMTree = xml.dom.minidom.parse(urllib.urlopen(URL))
    

def cancel():
    #if tkMessageBox.askokcancel("Quit", "Are you sure?"):
        root.destroy()
def search():    
    input_Land = tkSimpleDialog.askstring("Vær fra Yr.no", "Skriv Land\n")
    input_Fylke = tkSimpleDialog.askstring("Vær fra Yr.no", " Skriv Fylke\n")
    input_Kommune = tkSimpleDialog.askstring("Vær fra Yr.no", "Skriv Kommune\n")
    input_Sted = tkSimpleDialog.askstring("Vær fra Yr.no", "Skriv Sted\n")
    output=fetchXML(input_Land, input_Fylke, input_Kommune, input_Sted)
    collection = DOMTree.documentElement
    tkMessageBox.showinfo(collection.getElementByTagName('time')[20].attributes['from'].value
                          collection.getElementByTagName('time')[20].childNodes[11].attributes['mps'].value
                          collection.getElementByTagName('time')[20].childNodes[11].attributes['deg'].value)



search = Button(app, text = "Search", command = search)
search.grid(row=1, column=1)
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
