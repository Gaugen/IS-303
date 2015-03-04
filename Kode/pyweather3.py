import json,  urllib2, Tkinter, tkSimpleDialog, tkMessageBox

def fetchHTML(url):
    #URL = "http://openweathermap.org/data/2.1/find/name?q="+url
    URL = "http://api.openweathermap.org/data/2.5/weather?q="+url
    req = urllib2.Request(URL)
    response=urllib2.urlopen(req)
    return response.read()
def cancel():
    if tkMessageBox.askokcancel("Exit", "Are you sure?"):
        root.destroy()

root = Tkinter.Tk()
root.withdraw()

tkMessageBox.showinfo("About","Python Weather App \nUsing Open Weather Maps API")

input_location = tkSimpleDialog.askstring("Weather App", "Enter a Location\n")
output=fetchHTML(input_location)
data = json.loads(output)

#tkMessageBox.showinfo("Results", "Location: " + str(data['sys'][0]['country']) +
#"\n\nCountry: " + str(data['list'][0]['sys']['country']) + "\n\nLatitude: " + str(data['list'][0]['coord']['lat'])+
#"\n\nLongitude: " +str(data['list'][0]['coord']['lon']) + "\n\nTemperature: "+str(data['list'][0]['main']['temp']-273.15) +" C"+
#"\n\nHumidity: " + str(data['list'][0]['main']['humidity']) + " %"+
#"\n\nPressure: " + str(data['list'][0]['main']['pressure']) + " hPa"+
#"\n\nWind Speed: " + str(data['list'][0]['wind']['speed']) + " mps" +
#"\n\nWeather Description: " + str(data['list'][0]['weather'][0]['description']) )                                                     

tkMessageBox.showinfo("Results", "Location: " + str(data['name']) +
"\n\nCountry: "+ str(data['sys']['country']) +
"\n\nLongitude: " +str(data['coord']['lon']) + 
"\n\nTemperature: "+str(data['main']['temp']-273.15) +" C"+
"\n\nHumidity: " + str(data['main']['humidity']) + " %"+
"\n\nPressure: " + str(data['main']['pressure']) + " hPa"+
"\n\nWind Speed: " + str(data['wind']['speed']) + " mps" +
"\n\nWeather Description: " + str(data['weather'][0]['description']))

tkMessageBox.cancel("Exit", "Are you sure?")



