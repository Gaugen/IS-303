import urllib2
import urllib
import json
from string import capitalize
import Tkinter as tk
from xml.dom.minidom import parse
import xml.dom.minidom
from datetime import datetime, timedelta



f = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Flekkefjord,no")
wf_owm = json.load(f)




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
