import json,  urllib2, Tkinter, tkSimpleDialog, tkMessageBox

OWM = "http://api.openweathermap.org/data/2.5/forecast/daily?lat=35&lon=139&cnt=10&mode=json"
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

