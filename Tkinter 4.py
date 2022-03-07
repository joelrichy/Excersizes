from tkinter import *
root = Tk()
root.title("Using a abel to place an image")

root.geometry("2000x1000")  # string using x. No spaces
root.maxsize(2000, 1000)  # sets the max size of the window if someone resizes it

gif = PhotoImage(file="foundergif.gif")

image_label = Label(root, image=gif)
image_label.pack()

root.title("Gif")
computer = Label(root, bg="Lime", fg="White",
                text="This is a gif", font=("Times", 50, "italic"))
computer.pack()


root.mainloop()