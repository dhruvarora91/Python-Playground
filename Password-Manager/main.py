import json
from re import M
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def generate_password():
  
  password_entry.delete(0, END)

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  # password_list = []
  # for char in range(nr_letters):
  #   password_list.append(random.choice(letters))
  # for char in range(nr_symbols):
  #   password_list += random.choice(symbols)
  # for char in range(nr_numbers):
  #   password_list += random.choice(numbers)
  
  password_letters = [random.choice(letters) for _ in range(nr_letters)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

  password_list = password_letters + password_symbols + password_numbers
  random.shuffle(password_list)

  # password = ""
  # for char in password_list:
  #   password += char
  
  password = ''.join(password_list)

  password_entry.insert(0, password)
  pyperclip.copy(password)


def save():
  
  website_text = website_entry.get()
  email_text = email_entry.get()
  password_text = password_entry.get()
  new_data = {
    website_text: {
      "email": email_text,
      "password": password_text
    }
  }
  
  if website_text == "" or email_text == "" or password_text == "": 
    messagebox.showinfo(title="Empty input field", message="Some fields are empty")
    
  else:
    save_password = messagebox.askokcancel(title=website_text, message=f"Do you want to save?\nEmail: {email_text}\nPassword: {password_text}")
    
    if save_password:
      # with open("passwords.txt", mode="a") as file:
      #   file.write(f"{website_text} | {email_text} | {password_text} \n")
      # try:
      #   with open("passwords.json", "r") as file:
      #     # 1. Reading old data
      #     data = json.load(file)
      #     # 2. Updating old data with new data
      #     data.update(new_data)
      # except FileNotFoundError:
      #   data = new_data
      # finally:
      #   with open("passwords.json", "w") as file:
      #     # 3. Saving updated data
      #     json.dump(data, file, indent=2)
      
      try:
        with open("passwords.json", "r") as file:
          data = json.load(file)
      except FileNotFoundError:
        with open("passwords.json", "w") as file:
          json.dump(new_data, file, indent=2)
      else:
        data.update(new_data)
        with open("passwords.json", "w") as file:
          json.dump(data, file, indent=2)
      finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


def find_password():
  
  try:
    with open("passwords.json", "r") as file:
      data = json.load(file)
      website_name = data[website_entry.get()]
  except FileNotFoundError:
    messagebox.showerror(title="Error", message="No Data file found")
  except KeyError:
    messagebox.showerror(title="Error", message="No details for the website exist")
  else:
    messagebox.showinfo(title=website_name, message=f"Email: {website_name['email']} \nPassword: {website_name['password']}")


# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=45)
email_entry.insert(0, "name@email.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, width=20)
generate_password_button.grid(row=3, column=2)

search_button = Button(text="Search", command=find_password, width=20)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
