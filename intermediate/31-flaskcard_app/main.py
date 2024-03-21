from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

img_cross = PhotoImage(file="images/wrong.png")
btn_unknown = Button(image=img_cross, highlightthickness=0)
btn_unknown.grid(row=1, column=0)
img_check = PhotoImage(file="images/right.png")
btn_known = Button(image=img_check, highlightthickness=0)
btn_known.grid(row=1, column=1)

window.mainloop()