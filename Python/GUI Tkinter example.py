
from Tkinter import *

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
