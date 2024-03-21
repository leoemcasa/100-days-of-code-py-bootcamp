"""tkinter"""
import tkinter as tk
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {}
data_dict = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orignal_data = pd.read_csv("data/french_words.csv")
    data_dict = orignal_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
    

def next_card():
    """Next card"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = rd.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="Black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Back of the card"""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    

def known_word():
    """Known words"""
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

img_cross = tk.PhotoImage(file="images/wrong.png")
btn_unknown = tk.Button(image=img_cross, highlightthickness=0, command=next_card)
btn_unknown.grid(row=1, column=0)
img_check = tk.PhotoImage(file="images/right.png")
btn_known = tk.Button(image=img_check, highlightthickness=0, command=known_word)
btn_known.grid(row=1, column=1)

next_card()
window.mainloop()
