import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from ttkwidgets.autocomplete import AutocompleteCombobox
import random
from tables.tables_index import item_tables
from tables.tables_index import effects_tables
from tables.tables_index import encounter_tables
from tables.tables_index import experiences_tables
from tables.tables_index import name_tables
from tables.tables_index import crafting_tables
from tables.tables_index import location_tables
from tables.tables_index import events_tables
from tables.tables_index import quests_tables
from tables.tables_index import tables

def get_item_from_table(table_name, item_index, num_items):
    if table_name in tables:
        items = list(tables[table_name])

        if num_items > 1:
                result = random.sample(items, num_items)
        elif item_index == "":
            result = random.choice(items)
        else:
            result = items[int(item_index) - 1]

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
            result_text.insert(tk.END, f"- {item}\n")
    else:
        result_text.insert(tk.END, result)

    result_text.config(state=tk.DISABLED)

def update_table_selector(event):
    category = category_var.get()
    if category == "All":
        table_selector['values'] = list(tables.keys())
    else:
        filtered_tables = [table for table, cat in table_categories.items() if cat == category]
        table_selector['values'] = filtered_tables

app = tk.Tk()
app.title("D100 Table Roller")

table_categories = {}
for table_name in tables:
    if table_name in item_tables:
        table_categories[table_name] = "Items"
    elif table_name in effects_tables:
        table_categories[table_name] = "Effects"
    elif table_name in experiences_tables:
        table_categories[table_name] = "Experiences"
    elif table_name in encounter_tables:
        table_categories[table_name] = "Encounters"
    elif table_name in name_tables:
        table_categories[table_name] = "Names"
    elif table_name in location_tables:
        table_categories[table_name] = "Locations"
    elif table_name in crafting_tables:
        table_categories[table_name] = "Crafting Items"
    elif table_name in events_tables:
        table_categories[table_name] = "Events"
    elif table_name in quests_tables:
        table_categories[table_name] = "Quests"
    else:
        table_categories[table_name] = "Other"

# Input field
input_label = tk.Label(app, text="Enter a number (1-100):")
input_label.pack()
input_entry = tk.Entry(app)
input_entry.pack(pady=10)

# Table selector
table_label = tk.Label(app, text="Select a d100 table:")
table_label.pack()
table_var = StringVar()
table_selector = AutocompleteCombobox(app, textvariable=table_var, completevalues=list(tables.keys()))
table_selector.pack(pady=10)
table_selector.config(width=30)

# Category selector
category_var = StringVar()
category_label = tk.Label(app, text="Select a category:")
category_label.pack()

# Add "Select All" to categories
categories = ["All"] + list(set(table_categories.values()))
category_selector = ttk.Combobox(app, textvariable=category_var, values=categories)
category_selector.pack()
category_var.set("All")

category_selector.bind("<<ComboboxSelected>>", update_table_selector)

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
