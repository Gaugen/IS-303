import json,  urllib2, Tkinter, tkSimpleDialog, tkMessageBox
from Tkinter import *

def fetchHTMLYahoo(url):
    URL = "http://weather.hosting4real.net/"+url
    req = urllib2.Request(URL)
    response=urllib2.urlopen(req)
    return response.read()

def searchYahoo():    
    input_location = tkSimpleDialog.askstring("Weather App", "Enter a Location\n")
    output=fetchHTMLYahoo(input_location)
    data = json.loads(output)
    tkMessageBox.showinfo("Results", "Location: " + str(data['name']) +
                          "\n\nCountry: "+ str(data['sys']['country']) +
                           "\n\nLongitude: " +str(data['coord']['lon']) +
                           "\n\nTemperature: "+str(data['main']['temp']-273.15) +" C"+
                           "\n\nHumidity: " + str(data['main']['humidity']) + " %"+
                           "\n\nPressure: " + str(data['main']['pressure']) + " hPa"+
                           "\n\nWind Speed: " + str(data['wind']['speed']) + " mps" +
                           "\n\nWeather Description: " + str(data['weather'][0]['description']))


searchYahoo = Button(app, text = "Search on Yahoo Weather", command = searchYahoo)
searchYahoo.grid(row=3, column=3)
cancel = Button(app, text = "Cancel", command = cancel)
cancel.grid(row=2, column=2)

root.mainloop()
