import tkinter as tk
import random
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import ttk

from tables.tables_index import tables

def get_item_from_table(table_name, item_index, num_items):
    if table_name in tables:
        items = list(tables[table_name])

        if num_items > 1:
                result = random.sample(items, num_items)
        elif item_index == "":
            result = random.choice(items)
        else:
            result = items[int(item_index)-1]

        return result

def on_roll_click(num_items):
    table_name = table_var.get()
    if not table_name:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Select a table.")
        result_text.config(state=tk.DISABLED)
        return

    result = get_item_from_table(table_name, input_entry.get(), num_items)
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    if isinstance(result, list):
        for i, item in enumerate(result, 1):
            result_text.insert(tk.END, f"{item}\n")
    else:
        result_text.insert(tk.END, result)

    result_text.config(state=tk.DISABLED)

app = tk.Tk()
app.title("D100 Table Roller")

# Input field
input_label = tk.Label(app, text="Enter a number (1-100):")
input_label.pack()
input_entry = tk.Entry(app)
input_entry.pack(pady=10)

# Table selector
table_label = tk.Label(app, text="Select a d100 table:")
table_label.pack()
table_var = tk.StringVar()
table_selector = AutocompleteCombobox(app, textvariable=table_var, completevalues=list(tables.keys()))
table_selector.pack(pady=10)
table_selector.config(width=30)

# Roll buttons
button_frame = tk.Frame(app)
button_frame.pack()

roll_button = tk.Button(button_frame, text="Roll", command=lambda: on_roll_click(1))
roll_button.pack(side=tk.LEFT, padx=10)

roll_button_10 = tk.Button(button_frame, text="Roll 10", command=lambda: on_roll_click(10))
roll_button_10.pack(side=tk.LEFT, padx=10, pady=10)

# Output field
result_text = tk.Text(app, wrap=tk.WORD, height=12, width=40)
result_text.pack()
result_text.config(state=tk.DISABLED)

app.mainloop()
