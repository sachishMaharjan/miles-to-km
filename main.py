from tkinter import *


def calculate_function():
    """ Converts miles to kilometer"""
    input_value = float(input_entry.get())
    output_value = str(round(input_value * 1.6))
    output_label.config(text=output_value)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)


# Button
button = Button(text="Calculate", command=calculate_function)
button.grid(row=2, column=1)

# label
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(row=0, column=2)

km_label = Label(text="km", font=("Arial", 24, "bold"))
km_label.grid(row=1, column=2)

is_equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_label.grid(row=1, column=0)

output_label = Label(text="0", font=("Arial", 24, "bold"))
output_label.grid(row=1, column=1)

# Entry
input_entry = Entry(width=10)
input_entry.grid(row=0, column=1)


window.mainloop()
