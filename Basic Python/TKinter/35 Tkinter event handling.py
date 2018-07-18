"""
we will cover tkinter event handling in this part.
In this scenario, we are adding a quit event to our quit button, which currently does nothing when clicked on.
In basically every circumstance, we're going to want to have our buttons actually do something or perform an action rather than just appear there.
This is called an event when someone clicks on something, and we can write code to handle events.
Generally, we want to write code that is in line what the expectation of the user that created the event.
The more in-line your program can be with what the user intends to happen with their events, the more user-friendly it is going to be.

In tkinter, event handling is as simple as adding a command, which we'll make into a function.
Even though this function we create is a basic 1-line function that simply calls another function, we can see how we can later create more complex functions for our events.
"""
from tkinter import *


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Exit",command=self.client_exit)

        # placing the button on my window
        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)

#mainloop
root.mainloop()
