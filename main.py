from tkinter import *
from tkinter import messagebox
from password_gen import *
import pyperclip  # To copy data to clipboard automatically


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def make_password():
    generated_password = generate_password()
    password_enter.delete(0, END)
    password_enter.insert(0, generated_password)
    # Copy the generated password to clipboard
    pyperclip.copy(generated_password)
    messagebox.showinfo(title="saved", message="Password copied to clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_enter.get()
    user = user_name_enter.get()
    user_password = password_enter.get()

    if len(website) == 0 or len(user) == 0 or len(user_password) == 0:
        messagebox.showerror(title="Empty fields", message="Please fill the missing fields")
    else:
        consent = messagebox.askokcancel(title=website, message=f"These are the details entered:\nwebsite: {website}"
                                                                f"\nuser: {user}\npassword: {user_password}\n\nDo You want to save ?")

        if consent:
            with open("data.csv", "a") as hand:  # open file
                hand.write(f"{website},{user},{user_password}\n")

            messagebox.showinfo(title="Saving succeed", message="Your data has been saved")

            # delete entries
            website_enter.delete(0, END)
            user_name_enter.delete(0, END)
            password_enter.delete(0, END)

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

user_name_label = Label(text="Username/Email:", bg=DARK_INDIGO, fg="white")
user_name_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=DARK_INDIGO, fg="white")
password_label.grid(row=3, column=0)

# Entries
website_enter = Entry(width=35)
website_enter.grid(row=1, column=1, columnspan=2)
website_enter.focus()

user_name_enter = Entry(width=35)
user_name_enter.grid(row=2, column=1, columnspan=2)

password_enter = Entry(width=21)
password_enter.grid(row=3, column=1, )

# buttons
generate_password_button = Button(text="Generate Password", width=15, bg=LIGHT_INDIGO, command=make_password)
generate_password_button.grid(row=3, column=2)

add = Button(text="Add", width=32, bg=LIGHT_INDIGO, command=save)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()
