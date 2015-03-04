import json,  urllib2, Tkinter, tkSimpleDialog, tkMessageBox

root = Tkinter.Tk()
root.title("Weather App")
root.geometry("200x200")
app = Application(root)

class Application(Frame):
    """A Weather Application. """

    def __init__(self, master):
        """ Initialize the Frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Makes the widget that displays the buttons."""
        self.button1 = Button(self)
        self.button1["Text"] = "Search"
        self.button1["command"] = search
        self.button1.grid(row=0, column=1)
        self.button2 = Button(self)
        self.button2["Text"] = "Cancel App"
        self.button2["command"] = cancel
        self.button2.grid(row=0, column=2)
      
    def fetchHTML(url):
        URL = "http://api.openweathermap.org/data/2.5/weather?q="+url
        req = urllib2.Request(URL)
        response=urllib2.urlopen(req)
        return response.read()
    def cancel():
        if tkMessageBox.askokcancel("Quit", "Are you sure?"):
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


'''B1 = Tkinter.Button(root, text = "Cancel", command = cancel)
B1.grid(row=0, column=1)
B1.pack()
B2 = Tkinter.Button(root, text = "search", command = search)
B2.pack()'''


root.mainloop()

