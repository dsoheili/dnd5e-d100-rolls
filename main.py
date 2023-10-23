import tkinter as tk
import random
import re

from tables.tables_index import tables

def get_item_from_table(table_name, item_index):
    if table_name in tables:
        items = list(tables[table_name])

        if item_index == "":
            result = random.choice(items)
        else:
            result = items[int(item_index)-1]

        return result

def on_random_click():
    random_number = random.randint(1, 100)
    input_entry.delete(0, tk.END)
    input_entry.insert(0, random_number)

def on_roll_click():
    table_name = table_var.get()
    if not table_name:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Select a table.")
        result_text.config(state=tk.DISABLED)
        return

    result = get_item_from_table(table_name, input_entry.get())
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state=tk.DISABLED)

app = tk.Tk()
app.title("D100 Table Roller")

# Input field
input_label = tk.Label(app, text="Enter a number (1-100):")
input_label.pack()
input_entry = tk.Entry(app)
input_entry.pack()

# Random button
random_button = tk.Button(app, text="Random", command=on_random_click)
random_button.pack()

# Table selector
table_label = tk.Label(app, text="Select a d100 table:")
table_label.pack()
table_var = tk.StringVar()
table_selector = tk.OptionMenu(app, table_var, *tables.keys())
table_selector.pack()

# Roll button
roll_button = tk.Button(app, text="Roll", command=on_roll_click)
roll_button.pack()

# Output field
result_text = tk.Text(app, wrap=tk.WORD, height=10, width=40)
result_text.pack()
result_text.config(state=tk.DISABLED)

app.mainloop()
