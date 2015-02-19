import urllib2
import urllib
import json
from string import capitalize
import Tkinter as tk
from xml.dom.minidom import parse
import xml.dom.minidom
from datetime import datetime, timedelta
from Tkinter import *


f = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Flekkefjord,no")
wf_owm = json.load(f)

# Weather GUI

#create window
root = Tk()

#scale the window
root.title("Weather App")
root.geometry("500x300")

app = Frame(root)
app.grid()
label = Label(app, text = "this is a test")
label.grid()

button1 = Button(app, text = "This is a Button")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text ="this will show text")

button3 = Button(app)
button3.grid()

button3["text"] = "This will show up as well."

#kick off the event loop
root.mainloop()


#
#city = ''
#data = open('data.txt', 'r+')

#for i in data:
#    if 'current_city' in i:
#        index = len(i)
#        city = i[13:index]

#print city
#
#def kelvinToCelsius(kelvin_temp):
    #return str(int(kelvin_temp)-273) + ' Degree Celsius'
#
#def setText(string, string_var):
    #string_var.set(string)
#
#def getCurrentTemperature(city):
    #city = city.replace(' ', '%20')
    #url_to_call = 'http://api.openweathermap.org/data/2.5/weather?q=' + city
    #response = urllib2.urlopen(url_to_call)
    #json_obj = json.load(response)
    #print url_to_call
#
    #current_desc = capitalize(json_obj['weather'][0]['description'])
    #current_temp = kelvinToCelsius(json_obj['main']['temp'])
#
#
    #setText(city, city_name_label_text_var)
#
    #return current_desc + ': ' + current_temp
#
#maingui = tk.Tk()
#
#city_temp_and_desc_label_text_var = tk.StringVar()
#city_name_label_text_var = tk.StringVar()
#
#main_frame = tk.Frame(maingui, width=500, height=200, borderwidth=2)
#main_frame.pack()
#
#city_name_label = tk.Label(main_frame, textvariable=city_name_label_text_var, font=12).place(x=226, y=0)
#city_temp_and_desc_label = tk.Label(main_frame, textvariable=city_temp_and_desc_label_text_var, font=30).place(x=140, y=99)
#
#setText(getCurrentTemperature(city), city_temp_and_desc_label_text_var)
#
#tk.mainloop()
