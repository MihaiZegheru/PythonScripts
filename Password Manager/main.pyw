from tkinter import *
from tkinter import messagebox
import json
import pyperclip
import random

TEXT_FONT = ("Lucida Sans Unicode", 12)
BUTTON_FONT = ("Arial", 11)
INPUT_FONT = ("Arial", 11)
PASSWORD_DATA_FILE = "passwords_data.json"
EMAIL = ""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def get_data_from_file():
    with open(PASSWORD_DATA_FILE, 'r') as file:
        data = json.load(file)
    return data


def set_data_to_file(data):
    with open(PASSWORD_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def reset_fields():
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    username_entry.insert(0, EMAIL)
    password_entry.delete(0, END)
    website_entry.focus()


def search_data():
    try:
        data = get_data_from_file()
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="There is no data!")
    else:
        website_to_search = website_entry.get()
        username_to_search = username_entry.get()

        if len(website_to_search) == 0 or len(username_to_search) == 0:
            messagebox.showerror(title="Oops", message="Please fill in the Website and the Email/Username!")
            return

        try:
            if data[website_to_search.lower()]["email"] != username_to_search:
                messagebox.showerror(title="Oops", message="There is no data for this Email/Username!")
                return

            found_password = data[website_to_search.lower()]["password"]
            pyperclip.copy(found_password)
            messagebox.showinfo(title=website_to_search, message=f"The password for {username_to_search} "
                                                                 f"at {website_to_search} is:\n\n             "
                                                                 f"                       {found_password}\n\n"
                                                                 f"(the password was copied to your clipboard)")
        except KeyError:
            messagebox.showerror(title="Oops", message="There is no data for the information provided!")


def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please fill in all the fields!")
        return

    can_proceed = messagebox.askokcancel(title=website,
        message=f"These are the entered details:\nEmail/Username: {username}\nPassword: {password}\nProceed?\n"
                f"(the password was copied to your clipboard)")

    website = website.lower()

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    data = new_data
    if can_proceed:
        try:
            data = get_data_from_file()
            data.update(new_data)
        except FileNotFoundError:
            pass
        finally:
            set_data_to_file(data)
        reset_fields()


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=50)
window.resizable(0, 0)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.config(font=TEXT_FONT)
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.config(font=TEXT_FONT)
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", pady=10)
password_label.config(font=TEXT_FONT)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=24, font=INPUT_FONT, borderwidth=0.5)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = Entry(width=42, font=INPUT_FONT, borderwidth=0.5)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, EMAIL)
# Change cuz it s hardcoded (Ask user for their email at when app is first run?)

password_entry = Entry(width=24, font=INPUT_FONT, borderwidth=0.5)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", font=BUTTON_FONT, borderwidth=0.5, command=search_data, width=15)
search_button.grid(row=1, column=2)

random_generate_button = Button(text="Generate Password", font=BUTTON_FONT, borderwidth=0.5, command=generate_password)
random_generate_button.grid(row=3, column=2)

add_button = Button(width=37, text="Add", font=BUTTON_FONT, borderwidth=0.5, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
