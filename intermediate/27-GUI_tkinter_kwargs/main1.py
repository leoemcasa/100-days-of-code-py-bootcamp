import tkinter

window = tkinter.Tk()
window.title("My 1st python GUI")
window.minsize(500, 300)

my_label = tkinter.Label(text="1st Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")
my_label["text"] = "text"
my_label.config(text="New text")
my_label2 = tkinter.Label(text="2nd Label", font=("Arial", 16, "bold"))
my_label2.pack()


def button_clicked():
    my_label2.config(text=inpt.get())
    print("btn clicked")


button = tkinter.Button(text="Click here", command=button_clicked)
button.pack()

inpt = tkinter.Entry(width=10)
inpt.pack()

window.mainloop()