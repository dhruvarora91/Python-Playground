from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

def calculate():
  miles = float(miles_input.get())
  kilometer = miles * 1.609
  kilometer_result_label.config(text=f"{kilometer}")

is_equal_to_label = Label(text='is equal to')
is_equal_to_label.grid(row=1, column=0)

miles_label = Label(text='miles')
miles_label.grid(row=0, column=2)

kilometer_result_label = Label(text='0')
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text='km')
kilometer_label.grid(row=1, column=2)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()