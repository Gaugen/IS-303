from Tkinter import *

class Application(Frame):
    """AGUI application with three buttons. """

    def __init__(self, master):
        """ Initialize the Frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self) :
        """Create Widgets for movie type choice"""
        Label(self,
              text = "Choose your Favorite move type"
              ).grid(row = 0, column = 0, sticky = W)
        Label(self,
              text = "Select one:"
              ).grid(row = 1, column = 0, sticky = W)
        
        #variable for single, favorite type of movie
        self.favorite = StringVar()
        self.favorite.set("1")

        Radiobutton(self,
                    text = "Comedy",
                    variable = self.favorite,
                    value = "Comedy.",
                    command = self.update_text
                    ).grid(row=2, column=0, sticky =W)
        Radiobutton(self,
                    text = "Drama",
                    variable = self.favorite,
                    value = "Drama.",
                    command = self.update_text
                    ).grid(row=3, column=0, sticky =W)
        Radiobutton(self,
                    text = "Romance",
                    variable = self.favorite,
                    value = "Romance.",
                    command = self.update_text
                    ).grid(row=4, column=0, sticky =W)
        self.result = Text(self, width = 40, height = 5, wrap = WORD)
        self.result.grid(row =5, column = 0, columnspan = 3)

    def update_text(self):
        "Update text"
        message = "Your favorite type of movie is "
        message += self.favorite.get()

        self.result.delete(0.0, END)
        self.result.insert(0.0, message)

root = Tk()
root.title("Movie chooser 2")
app = Application(root)
root.mainloop()
