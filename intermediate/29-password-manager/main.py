from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    entr_pass.delete(0, END)
    entr_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = entr_site.get()
    mail = entr_mail.get()
    passw = entr_pass.get()
    if len(site) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Ooops", message="All fields are required")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"is it ok to save {mail}?")
        if is_ok:
            with open("data.txt", "a") as datafile:
                datafile.write(f"{site}, {mail}, {passw}\n")
            entr_site.delete(0, END)
            entr_pass.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(row=0, column=1)

lbl_site = Label(text="Website")
lbl_site.grid(row=1, column=0, sticky=W)
lbl_mail = Label(text="E-mail")
lbl_mail.grid(row=2, column=0, sticky=W)
lbl_pass = Label(text="Password")
lbl_pass.grid(row=3, column=0, sticky=W)

entr_site = Entry(width=38)
entr_site.grid(row=1, column=1, columnspan=2, sticky=W, padx=12)
entr_site.focus()
entr_mail = Entry(width=38)
entr_mail.grid(row=2, column=1, columnspan=2, sticky=W, padx=12)
entr_mail.insert(0, "yourmail@gmail.com")
entr_pass = Entry(width=29)
entr_pass.grid(row=3, column=1, sticky=W, padx=12)

btn_genpass = Button(text="Gen", command=generate_passw)
btn_genpass.grid(row=3, column=2, sticky=W)
btn_add = Button(text="Add", width=32, command=save)
btn_add.grid(row=4, column=1, columnspan=2)


window.mainloop()