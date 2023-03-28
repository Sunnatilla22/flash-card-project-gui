from tkinter import *
import pandas
import random
import csv

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

#----------------------------Button setup---------------------------------#

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# print(new_dict)
# print(new_dict[0]["French"])
# rand_word = new_dict[random.randint(1, 103)][random.choice(["French", "English"])]

# print(new_dict[random.randint(1, 103)]["French"])
# print(random.choice(to_learn))

# #Creating CSV file
# df = pandas.DataFrame(to_learn)
# n_data = df.to_csv('words_to_learn.csv', index=False)
# read_new_data = pandas.read_csv('words_to_learn.csv')
#
# words_to_learn = read_new_data.to_dict(orient="records")
#
# # print(words_to_learn)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)



def is_known():
    print(current_card)
    to_learn.remove(current_card)
    print(to_learn)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)

    next_card()



# def is_known():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     # current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     # canvas.itemconfig(card_word, text=current_card["French"], fill="black")
#     canvas.itemconfig(card_background, image=card_front)
#     flip_timer = window.after(3000, flip_card)
#
#     try:
#         current_card = random.choice(words_to_learn)
#     except FileNotFoundError:
#         current_card = random.choice(to_learn)
#     else:
#         canvas.itemconfig(card_word, text=current_card["French"], fill="black")
#         if known_button:
#             print(current_card)
#             words_to_learn.remove(current_card)
#             print(words_to_learn)
#             df = pd.DataFrame(words_to_learn)
#             n_data = df.to_csv('words_to_learn.csv', index=False)

    #Sunnat's way of flipping
    # if next_card:
    #     flip_timer = window.after(3000, flip_card)
    # if not next_card:
    #     window.after_cancel(flip_timer)
#----------------------------UI SETUP---------------------------------#
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Angela's way of flipping
flip_timer = window.after(3000, flip_card)

canvas = Canvas(height=528, width=800, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 270, image= card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="./images/wrong.png")
unkown_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unkown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button= Button(image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()