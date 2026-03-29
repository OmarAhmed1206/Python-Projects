from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT = ("Arial",12,"bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def add_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_character = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_character = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    symbol_character = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = letter_character + password_character + symbol_character

    random.shuffle(password_list)

    password = "".join(password_list)
    password_text_box.delete(0,END)
    password_text_box.insert(0,f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry = website_text_box.get()
    email_entry = email_text_box.get()
    password_entry = password_text_box.get()

    new_data = {
        website_entry: {
            "Email" : email_entry,
            "Password": password_entry
        }
    }

    if len(website_entry) == 0 or len(email_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title="error", message="Cannot Save Empty Boxes, Please Fill In")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except  (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_text_box.delete(0, END)
            password_text_box.delete(0,END)

def find_password():
    website_entry = website_text_box.get()
    if len(website_entry) == 0:
        messagebox.showinfo(title="error", message="Please Fill In The Website Box")
    else:
        try:
                with open("data.json", "r")as data_file:
                    data = json.load(data_file)
        except  (FileNotFoundError, json.JSONDecodeError):
                messagebox.showinfo(title="Error", message="File Not Found/Documented")
        else:
            if website_entry in data:
                email = data[f"{website_entry}"]["Email"]
                password = data[f"{website_entry}"]["Password"]
                messagebox.showinfo(title="Found", message = f"Email/Username: {email}\nPassword:{password}")
            else:
                messagebox.showinfo(title="Error", message="Website Not Found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
canvas = Canvas(height=200, width=200)
Pass_image = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image=Pass_image)
window.config(padx=50,pady=50)
canvas.grid(column=1,row=0)

# ---------------------------- LABEL SETUP ------------------------------- #
website_label = Label(font=FONT, text="Website: ")
website_label.grid(column=0,row=1)

email_label = Label(font=FONT, text="Email/Username: ")
email_label.grid(column=0,row=2)

password_label = Label(font=FONT,text="Password: ")
password_label.grid(column=0,row=3)

# ---------------------------- ENTRY SETUP ------------------------------- #
website_text_box = Entry(width=29)
website_text_box.grid(column=1,row=1,pady=2,padx=2)
website_text_box.focus()

email_text_box = Entry(width=35)
email_text_box.grid(column=1,row=2,columnspan=2)
email_text_box.focus()
email_text_box.insert(END, "omarglobal2@gmail.com")

password_text_box = Entry(width=25)
password_text_box.grid(column = 1, row=3,columnspan=2)
password_text_box.focus()

# ---------------------------- BUTTON SETUP ------------------------------- #
generate_password_button = Button(text="Generate Password", command=add_pass)
generate_password_button.grid(column = 3, row=3,columnspan=2,padx=5,pady=5)

add_button = Button(text="Add",width=36, command = save)
add_button.grid(column = 1, row=4,columnspan=2)

search_button = Button(text="KNN",width=12,command=find_password)
search_button.grid(column=2,row=1,columnspan=2,padx=5,pady=5)

window.mainloop()