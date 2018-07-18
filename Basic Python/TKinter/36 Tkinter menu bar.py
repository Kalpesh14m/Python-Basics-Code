"""
Now that we've got the basic window, buttons, and event handling down, we're ready to tackle the idea of a menu bar.
The way tkinter works, along with quite a few graphics/windows operations work, is with a main window, then you sort of build things on top of it, then display everything all at once, which gives the appearance of a singular package.
What makes tkinter most confusing, at least to me, is that you have to work both forwards and backwards in relation to your goal.

So, when I make programs, I usually work backwards from my goal.
I know what the end objective is going to be, and then I take steps in reverse, first calling a non-existent function as if it works how I might need it to, then I define it to fit how I need it to act.
With tkinter, this methodology is used as well, only you have to do some of the beginning steps, then you have to go to the end and work backwards.
Let's hit the code to understand better:
"""

# Simple enough, just import everything from tkinter.
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

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        #adding new button in menue bar it is working bottom-up structure
        #if you want to add new button then just add_command and set it's label and command
        file.add_command(label="Save")
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)


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
