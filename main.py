from tkinter import *
from tkinter import messagebox
from password_gen import *
import json
import pyperclip  # To copy data to clipboard automatically


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def make_password():
    generated_password = generate_password()
    password_enter.delete(0, END)
    password_enter.insert(0, generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_csv():
    return state.get()


def save():
    website = website_enter.get()
    user_email = email_enter.get()
    user_password = password_enter.get()
    
    #  Check for missing values
    if len(website) == 0 or len(user_email) == 0 or len(user_password) == 0:
        messagebox.showerror(title="Empty fields", message="Please fill the missing fields")
    else:
        consent = messagebox.askokcancel(title=website, message=f"These are the details entered:\nwebsite: {website}\n"
                                                                f"user: {user_email}\npassword: {user_password}\n\n"
                                                                f"Do You want to save ?")

        if consent:  # when the user confirms the entered info
            data = {
                website: {
                    'email': user_email,
                    'password': user_password
                }
            }

            try:
                with open("data.json", "r") as data_file:  # open file
                    fetched_data = json.load(data_file)
            except FileNotFoundError or json.decoder.JSONDecodeError:  # if no json file is found ==> Create a new file
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                fetched_data.update(data)
                with open("data.json", "w") as data_file:
                    json.dump(fetched_data, data_file, indent=4)

            # if "Add to .csv" is checked ==> save the entered data into data.csv
            if save_csv():
                with open("data.csv", "a") as data_file:
                    data_file.write(f"{website},{user_email},{user_password}\n")

            messagebox.showinfo(title="Saving succeed", message="Your data has been saved")

            # clear entries
            website_enter.delete(0, END)
            email_enter.delete(0, END)
            password_enter.delete(0, END)

# ----------------------- SEARCH FOR A WEBSITE DATA ---------------------- #


def find_website():
    website = website_enter.get()
    try:
        with open("data.json", "r") as data_file:  # open file
            # hand.write(f"{website},{user},{user_password}\n")
            loaded_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Data File Missing", message="Data File not Found or deleted")
    else:
        if website in loaded_data:
            user_email = loaded_data[website]['email']
            user_password = loaded_data[website]['password']

            # Copy password to clipboard
            pyperclip.copy(user_password)

            messagebox.showinfo(title=website, message=f"user: {user_email}\npassword: {user_password}\n\n"
                                                       f">> Password copied to clipboard !!")

        elif len(website) == 0:
            messagebox.showerror(title="Blank field", message="Enter a valid website name")
        else:
            messagebox.showinfo(title="website not found", message="No details found for this website\n"
                                                                   "It is not in the database")

# ---------------------------- UI SETUP ------------------------------- #


# Color
DARK_INDIGO = "#2f2454"
LIGHT_INDIGO = "#7678a6"

# window setup
window = Tk()
window.title("Magician Password Manager")
window.config(padx=30, pady=30, bg=DARK_INDIGO)

# Setting canvas to view logo
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=DARK_INDIGO)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:", bg=DARK_INDIGO, fg="white")
website_label.grid(row=1, column=0)

user_name_label = Label(text="Email / User Name:", bg=DARK_INDIGO, fg="white")
user_name_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=DARK_INDIGO, fg="white")
password_label.grid(row=3, column=0)

# Entries
website_enter = Entry(width=32)
website_enter.grid(row=1, column=1)
website_enter.focus()

email_enter = Entry(width=51)
email_enter.grid(row=2, column=1, columnspan=2)

password_enter = Entry(width=32)
password_enter.grid(row=3, column=1)

# buttons
generate_password_button = Button(text="Generate Password", width=15, bg=LIGHT_INDIGO, activebackground=LIGHT_INDIGO, command=make_password)
generate_password_button.grid(row=3, column=2)

add = Button(text="Add", width=27, bg=LIGHT_INDIGO, activebackground=LIGHT_INDIGO, command=save)
add.grid(row=4, column=1)

search_button = Button(text="Search", width=15, bg=LIGHT_INDIGO, activebackground=LIGHT_INDIGO, command=find_website)
search_button.grid(row=1, column=2)

# csv checkbox
state = IntVar()
add_csv = Checkbutton(text="Add to .csv", variable=state, command=save_csv, bg=DARK_INDIGO, activebackground=DARK_INDIGO,
                      fg="white", activeforeground="white", selectcolor=LIGHT_INDIGO)
add_csv.grid(row=4, column=2)


window.mainloop()
