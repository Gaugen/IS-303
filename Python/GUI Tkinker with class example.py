#demonstrate how to use a class with TKinker

from Tkinter import *

class Application(Frame):
    """AGUI application with three buttons. """

    def __init__(self, master):
        """ Initialize the Frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create 3 buttons that do nothing. """
        #create first button
        self.button1 = Button(self, text = "Button1")
        self.button1.grid()
        
        #create button2
        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text = "Button2")

        #create button3
        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"] = "Button3"
root = Tk()
root.title("GUI eksempel")
root.geometry("200x85")

app = Application(root)

root.mainloop()     
