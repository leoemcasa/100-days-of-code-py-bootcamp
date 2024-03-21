from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    new_data = {
        site: {
            "email": mail,
            "password": passw
        }
    }
    if len(site) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Ooops", message="All fields are required")
    else:
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)  # gera um dict
        except FileNotFoundError:
            with open("data.json", "w") as datafile:
                json.dump(new_data, datafile, indent=4)
        else:
            data.update(new_data)

            with open("data.json", 'w') as datafile:
                json.dump(data, datafile, indent=4)
        finally:
            entr_site.delete(0, END)
            entr_pass.delete(0, END)

def search():
    site = entr_site.get()
    if len(site) == 0:
        messagebox.showwarning(title="Ooops", message="Website required")
    else:
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)  # gera um dict
        except FileNotFoundError:
            with open("data.json", "w") as datafile:
                messagebox.showwarning(title="Ooops", message="Datafile not found. An empty one was created")
        else:
            with open("data.json", 'r') as datafile:
                try:
                    data = json.load(datafile)
                    result = data[site]
                except KeyError:
                    messagebox.showinfo(title="Ooops", message="No site found")
                else:
                    messagebox.showinfo(title=f"Site: {site}", message=f"Usuário: {result["email"]}\nSenha: {result["password"]}")
                    pyperclip.copy(result["password"])
                finally:
                    entr_site.delete(0, END)
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

entr_site = Entry(width=30)
entr_site.grid(row=1, column=1, sticky=W, padx=6)
entr_site.focus()
entr_mail = Entry(width=30)
entr_mail.grid(row=2, column=1, columnspan=2, sticky=W, padx=6)
entr_mail.insert(0, "yourmail@gmail.com")
entr_pass = Entry(width=30)
entr_pass.grid(row=3, column=1, sticky=W, padx=6)

btn_genpass = Button(text="Passw", command=generate_passw)
btn_genpass.grid(row=3, column=2, sticky=W)
btn_add = Button(text="Add", width=33, command=save)
btn_add.grid(row=4, column=1, columnspan=2, padx=5)
btn_search = Button(text="find", command=search, width=5)
btn_search.grid(row=1, column=2, sticky=W)

window.mainloop()