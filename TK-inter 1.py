from tkinter import *
root = Tk()
# change name of window
root.title("My first window")

root.geometry("600x800")  # string using x. No spaces
root.maxsize(800, 400)  # sets the max size of the window if someone resizes it

#adding label widget
greeting = Label(text="Hello, Tkinter")

# need to use .pack() to get label to show
greeting.pack()

root.mainloop()
