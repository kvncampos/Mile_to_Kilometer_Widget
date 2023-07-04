from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)


# Button
def calculate_action() -> float:
    """Calculates Miles -> Km"""
    miles = entry.get()
    try:
        km = float(miles) * 1.609344
        is_equal.config(text=km)
        return km
    except ValueError:
        pass


def reset_action():
    """Resets the values of the Miles Entry and Km Calculation to Blank."""
    is_equal.config(text="0")
    entry.delete(0, END)


# Empty Entry
empty_label = Label()
empty_label.grid(row=0, column=0, padx=60)

# Entry
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="")
# entry.get()
entry.grid(row=0, column=1)
print(entry.get())

# Miles Label
mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

# is Equal to
is_equal = Label(text="is equal to")
is_equal.grid(row=1, column=0)

# is Equal to ---> This Changes to the final calculation.
is_equal = Label(text="")
is_equal.grid(row=1, column=1)

# Km
km = Label(text="Km")
km.grid(row=1, column=2)

# Calculate Button
calculate_button = Button(text="Calculate", command=calculate_action)
calculate_button.grid(row=2, column=1)

# Reset Button
reset_button = Button(text="Reset", command=reset_action)
reset_button.grid(row=2, column=2)

window.mainloop()
