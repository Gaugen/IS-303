import json,  urllib2, Tkinter, tkSimpleDialog, tkMessageBox
from Tkinter import *

root = Tk()
root.title("Weather App")
root.geometry()
app = Frame(root)
app.grid()
      
def fetchHTML(url):
    URL = "http://api.openweathermap.org/data/2.5/weather?q="+url
    req = urllib2.Request(URL)
    response=urllib2.urlopen(req)
    return response.read()
def cancel():
    #if tkMessageBox.askokcancel("Quit", "Are you sure?"):
        root.destroy()
def search():    
    input_location = tkSimpleDialog.askstring("Weather App", "Enter a Location\n")
    output=fetchHTML(input_location)
    data = json.loads(output)
    tkMessageBox.showinfo("Results", "Location: " + str(data['name']) +
                          "\n\nCountry: "+ str(data['sys']['country']) +
                           "\n\nLongitude: " +str(data['coord']['lon']) +
                           "\n\nTemperature: "+str(data['main']['temp']-273.15) +" C"+
                           "\n\nHumidity: " + str(data['main']['humidity']) + " %"+
                           "\n\nPressure: " + str(data['main']['pressure']) + " hPa"+
                           "\n\nWind Speed: " + str(data['wind']['speed']) + " mps" +
                           "\n\nWeather Description: " + str(data['weather'][0]['description']))



search = Button(app, text = "Search", command = search)
search.grid(row=1, column=1)
cancel = Button(app, text = "Cancel", command = cancel)
cancel.grid(row=2, column=2)

'''B1 = Tkinter.Button(root, text = "Cancel", command = cancel)
B1.grid(row=0, column=1)
B1.pack()
B2 = Tkinter.Button(root, text = "search", command = search)
B2.pack()'''


root.mainloop()



