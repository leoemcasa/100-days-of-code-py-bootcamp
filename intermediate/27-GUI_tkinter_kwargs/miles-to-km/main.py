import tkinter as tk


def miles_to_km():
    mil_to_km = round((int(inpt.get()) * 1.609344), 2)
    label_res.config(text=mil_to_km)
    # print("btn clicked")


window = tk.Tk()
window.title("Miles to Km converter")
window.minsize(500, 300)
window.config(padx=50, pady=50)

# Label
label_equal = tk.Label(text="is equal to", font=("Arial", 16, "bold"))
label_equal.grid(column=0, row=1)

label_miles = tk.Label(text="Miles", font=("Arial", 16, "bold"))
label_miles.config(padx=10, pady=0)
label_miles.grid(column=2, row=0)

label_km = tk.Label(text="Km", font=("Arial", 16, "bold"))
label_km.grid(column=2, row=1)

label_res = tk.Label(text="0", font=("Arial", 16, "bold"))
label_res.config(padx=0, pady=10)
label_res.grid(column=1, row=1)

# Button
button = tk.Button(text="Calculate", command=miles_to_km)
# button.config(padx=0, pady=20)
button.grid(column=1, row=2)

inpt = tk.Entry(width=10)
inpt.grid(column=1, row=0)

window.mainloop()