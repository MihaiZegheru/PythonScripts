from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
STREAKS_COLOR = "#40A264"
DATA_FILES_PATH = "./data"
FRENCH_DATA_FILE_PATH = DATA_FILES_PATH + "/french_words.csv"
IMAGES_FILES_PATH = "./images"
CARD_BACK_PATH = IMAGES_FILES_PATH + "/card_back.png"
CARD_FRONT_PATH = IMAGES_FILES_PATH + "/card_front.png"
RIGHT_PATH = IMAGES_FILES_PATH + "/right.png"
WRONG_PATH = IMAGES_FILES_PATH + "/wrong.png"
FIRE_PATH = IMAGES_FILES_PATH + "/fire.png"
TIME = 3
cool_down_on = False
data = None
index = None
offset = 6
LIMIT = 20

LANGUAGE_FONT = ("Ariel", 35, "italic")
WORD_FONT = ("Ariel", 55, "bold")
STREAKS_FONT = ("Ariel", 30, "bold")


def weighted_random():
    num = random.randint(1, 100)
    if num < 75:
        return random.randint(0, LIMIT)
    else:
        return random.randint(0, file_lines)


def get_word_data():
    global data
    # row = random.randint(1, file_lines - 1)
    # rows_to_skip = [r for r in range(1, file_lines) if r != row]
    data = pandas.read_csv(FRENCH_DATA_FILE_PATH, index_col=False)
    data = data.to_dict(orient="records")
    return data


def flip_card(language, word):
    global cool_down_on
    card.itemconfig(card_image, image=card_back_image)
    card.itemconfig(card_title, text=language, fill="white")
    card.itemconfig(card_word, text=word, fill="white")
    cool_down_on = False


def show_next_word():
    global timer
    global data
    global index
    global cool_down_on

    window.after_cancel(timer)
    cool_down_on = True

    index = weighted_random()
    row = data[index]

    languages = [lg for lg in row]

    foreign_language = languages[0]
    translated_language = languages[1]
    # I ll hard code that the first language is the foreign one
    foreign_word = row[foreign_language]
    translated_word = row[translated_language]

    # The foreign part
    card.itemconfig(card_image, image=card_front_image)
    card.itemconfig(card_title, text=foreign_language, fill="black")
    card.itemconfig(card_word, text=foreign_word, fill="black")

    timer = window.after(1000 * TIME, flip_card, translated_language, translated_word)


def count_file_lines(file):
    num_lines = sum(1 for line in open(file))
    return num_lines


def guessed_right():
    global index
    global data
    global guessed_streak

    if cool_down_on is False:
        guessed_streak += 1
    new_data = []
    new_index = index

    streaks.itemconfig(streaks_number_text, text=str(guessed_streak))

    if index + offset > LIMIT >= index:
        new_index = index + 50

    if index is not None:
        new_data.extend(data[:index])
        new_data.extend(data[index+1:new_index+1+offset])
        new_data.append(data[index])
        new_data.extend(data[new_index+1+offset:])
        index = None

    data = new_data
    show_next_word()


def guessed_wrong():
    global index
    global data
    global guessed_streak

    guessed_streak = 0
    streaks.itemconfig(streaks_number_text, text=str(guessed_streak))
    new_data = []

    if index is not None:
        new_data.append(data[index])
        new_data.extend(data[:index])
        new_data.extend(data[index+1:])
        index = None

    data = new_data
    show_next_word()


def on_closing():
    window.destroy()
    data_to_save = pandas.DataFrame(data)
    data_to_save.to_csv(FRENCH_DATA_FILE_PATH, index=None)


file_lines = count_file_lines(FRENCH_DATA_FILE_PATH)
guessed_streak = 0

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card App")

get_word_data()
timer = window.after(0, show_next_word)

streaks = Canvas(height=100, width=400, bg=BACKGROUND_COLOR, highlightthickness=0)
streaks.create_text(150, 50, font=STREAKS_FONT, text="Streaks:", fill=STREAKS_COLOR)
streaks_number_text = streaks.create_text(270, 50, font=STREAKS_FONT, text="0", fill=STREAKS_COLOR)
fire_image = PhotoImage(file=FIRE_PATH).subsample(2, 2)

streaks_image = streaks.create_image(330, 43, image=fire_image)
streaks.grid(row=0, column=1)

card_front_image = PhotoImage(file=CARD_FRONT_PATH)
card_back_image = PhotoImage(file=CARD_BACK_PATH)

card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(400, 263, image=card_front_image)
card_title = card.create_text(400, 150, font=LANGUAGE_FONT, text="Language")
card_word = card.create_text(400, 270, font=WORD_FONT, text="word")
card.grid(row=1, column=0, columnspan=3, pady=50, padx=50)

wrong_image = PhotoImage(file=WRONG_PATH)
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0.5, command=guessed_wrong)
wrong_button.grid(row=2, column=0)

right_image = PhotoImage(file=RIGHT_PATH)
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0.5, command=guessed_right)
right_button.grid(row=2, column=2)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
