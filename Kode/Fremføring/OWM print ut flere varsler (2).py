# coding=utf-8
import json,  urllib2, Tkinter, tkSimpleDialog, tkMessageBox, datetime

"""
Bruker metric som units, får da celsius for tempratur og km/s for speed
Hvis flere dager er ønskelig kan du endre cnt=5 til for eksempel cnt=7 (7 dager)
"""
def fetchHTML(url):
    URL = "http://api.openweathermap.org/data/2.5/forecast/daily?q=" + url + "&mode=json&units=metric&cnt=5"
    req = urllib2.Request(URL)
    response=urllib2.urlopen(req)
    return response.read()

"""
bruker datetime for å omkode unix time til dato (bibliotek importert). 
Datoene vises i window title. 
"""
def listdays(dayList):
    for day in dayList:
        tkMessageBox.showinfo(
        datetime.datetime.fromtimestamp(day['dt']).strftime('%d.%m.%Y'), 
        "Location: " +str(data['city']['name']) +
        "\n\nCountry: " +str(data['city']['country']) +
        "\n\nLongitude: " +str(data['city']['coord']['lon']) + 
        "\n\nTemperature: " +str(day['temp']['day']) +" C"+
        "\n\nHumidity: " + str(day['humidity']) + " %"+
        "\n\nPressure: " + str(day['pressure']) + " hPa"+
        "\n\nWind Speed: " + str(day['speed']) + " km/s" +
        "\n\nWeather Description: " + str(day['weather'][0]['description']))

root = Tkinter.Tk()
root.withdraw()

tkMessageBox.showinfo("About","Python Weather App \nUsing Open Weather Maps API")

input_location = tkSimpleDialog.askstring("Weather App", "Enter a Location\n")

output = fetchHTML(input_location)
data = json.loads(output)

# Print ut et json objekt av alle dagene (pretty printing)
#print json.dumps(data['list'], indent=2, sort_keys=True)

# data['list'] inneholder alle dagene som blir hentet fra openweathermap
listdays(data['list'])


