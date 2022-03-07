from tkinter import *
root = Tk()


root.geometry("2000x1000")  # string using x. No spaces
root.maxsize(2000, 1000)  # sets the max size of the window if someone resizes it

root.title("Computer")
computer = Label(root, bg="Lime", fg="White",
                text="Computer", font=("Times", 50, "italic"))
computer.pack()

root.title("Science is")
science = Label(root, bg="Blue", fg="Yellow",
                text="science is", font=("Times", 50, "bold"))
science.pack()

root.title("awesome")
awesome = Label(root, bg="Orange", fg="Red",
                text="awesome", font=("Times", 50))
awesome.pack()


root.mainloop()