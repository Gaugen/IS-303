#demonstrate how to use a class with TKinker

from Tkinter import *

class Application(Frame):
    """AGUI application with three buttons. """

    def __init__(self, master):
        """ Initialize the Frame"""
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 0 #counts button clicks
        self.create_widgets()

    def create_widgets(self):
        """Create button that counts buttonclicks """
      self.button = Button(self)
      self.button["Text"] = "Total Clicks: 0"
      self.button["command"] = self.update_count
      self.button.grid()

    def update_count(self):
        "increase count on button clicks"
        self.button_clicks + 1
        self.button["Text"] = "Total Clicks: " + str(self.button_clicks)
        

        
root = Tk()
root.title("GUI eksempel")
root.geometry("200x85")

app = Application(root)

root.mainloop()     
