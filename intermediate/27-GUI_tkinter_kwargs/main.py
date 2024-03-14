import tkinter as tk


def button_clicked():
    my_label2.config(text=inpt.get())
    print("btn clicked")


window = tk.Tk()
window.title("My 1st python GUI")
window.minsize(500, 300)
window.config(padx=15, pady=15)

# Label
my_label2 = tk.Label(text="2nd Label", font=("Arial", 16, "bold"))
my_label2.config(padx=15, pady=15)
my_label2.grid(column=0, row=0)

# Button
button = tk.Button(text="Click here", command=button_clicked)
button.grid(column=1, row=1)

button2 = tk.Button(text="Click here", command=button_clicked)
button2.grid(column=2, row=0)

inpt = tk.Entry(width=10)
inpt.grid(column=3, row=2)

window.mainloop()