#!/usr/bin/env python3
"""
D100 Table Roller - Clean Minimal UI
A sleek, minimal table rolling application for tabletop RPGs
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import os
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re
import datetime

class TableManager:
    """Handles loading and managing table files with dynamic category detection"""
    
    def __init__(self, tables_dir: str = "tables"):
        self.tables_dir = Path(tables_dir)
        self.tables: Dict[str, Dict[str, List[str]]] = {}
        self.config_file = self.tables_dir / "config.json"
        self.load_config()
        self.scan_tables()
    
    def load_config(self):
        """Load configuration for table categories and metadata"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            except Exception as e:
                print(f"Error loading config: {e}")
                self.config = {}
        else:
            self.config = {}
    
    def format_category_name(self, directory_name: str) -> str:
        """Convert directory name to proper category display name"""
        # Check if we have a mapping in config
        if 'categories' in self.config and directory_name in self.config['categories']:
            return self.config['categories'][directory_name]
        
        # Otherwise, format the directory name nicely
        # Replace underscores with spaces and title case
        formatted = directory_name.replace('_', ' ').title()
        
        # Handle special cases for better formatting
        replacements = {
            'Npcs': 'NPCs',
            'Ai': 'AI', 
            'Ui': 'UI',
            'Dnd': 'D&D',
            'Phb': 'PHB',
            'Gp': 'GP',
            'Dms': 'DMs',
            'Pc': 'PC',
            'Npc': 'NPC'
        }
        
        for old, new in replacements.items():
            formatted = formatted.replace(old, new)
        
        return formatted
    
    def format_table_name(self, filename: str) -> str:
        """Format filename into a proper table name"""
        # Replace underscores with spaces and title case
        formatted = filename.replace('_', ' ').title()
        
        # Handle special abbreviations and common gaming terms
        replacements = {
            'Phb': 'PHB',
            'Gp': 'GP', 
            'Npcs': 'NPCs',
            'Npc': 'NPC',
            'Dnd': 'D&D',
            'Dms': 'DMs',
            'Dm': 'DM',
            'Pc': 'PC',
            'Hp': 'HP',
            'Ac': 'AC',
            'Xp': 'XP'
        }
        
        for old, new in replacements.items():
            # Use word boundaries to avoid partial replacements
            import re
            pattern = r'\b' + re.escape(old) + r'\b'
            formatted = re.sub(pattern, new, formatted, flags=re.IGNORECASE)
        
        return formatted
    
    def scan_tables(self):
        """Scan the tables directory for .txt files and organize by category"""
        self.tables = {}
        
        if not self.tables_dir.exists():
            self.tables_dir.mkdir(parents=True, exist_ok=True)
            return
        
        # Scan for table files
        for file_path in self.tables_dir.rglob("*.txt"):
            # Skip report and config files
            if file_path.name in ["reorganization_report.txt", "readme.txt"]:
                continue
                
            relative_path = file_path.relative_to(self.tables_dir)
            
            # Determine category from folder structure
            if len(relative_path.parts) > 1:
                category_folder = relative_path.parts[0]
                category = self.format_category_name(category_folder)
            else:
                category = "Uncategorized"
            
            # Get table name from filename
            table_name = self.format_table_name(file_path.stem)
            
            # Load table contents
            try:
                table_contents = self.load_table_file(file_path)
                if table_contents:
                    if category not in self.tables:
                        self.tables[category] = {}
                    self.tables[category][table_name] = table_contents
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
    
    def load_table_file(self, file_path: Path) -> List[str]:
        """Load a single table file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
                return lines
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return []
    
    def get_categories(self) -> List[str]:
        """Get list of all categories"""
        return sorted(self.tables.keys())
    
    def get_tables_in_category(self, category: str) -> List[str]:
        """Get list of tables in a specific category"""
        return sorted(self.tables.get(category, {}).keys())
    
    def get_table(self, category: str, table_name: str) -> Optional[List[str]]:
        """Get a specific table"""
        return self.tables.get(category, {}).get(table_name)
    
    def create_sample_tables(self):
        """Create sample table files for demonstration in new structure"""
        sample_tables = {
            "weapons_armor/basic_weapons.txt": [
                "Rusty Dagger",
                "Iron Sword", 
                "Silver Blade",
                "Enchanted Bow",
                "Battle Axe",
                "War Hammer",
                "Crossbow",
                "Spear",
                "Mace",
                "Scimitar"
            ],
            "encounters/forest_encounters.txt": [
                "Wolves (1d4)",
                "Bandits (1d6)", 
                "Mysterious Traveler",
                "Ancient Tree",
                "Hidden Cave",
                "Goblin Patrol",
                "Wild Boar",
                "Fairy Ring",
                "Lost Child",
                "Treasure Chest"
            ],
            "names/tavern_names.txt": [
                "The Prancing Pony",
                "The Dragon's Rest",
                "The Singing Sword", 
                "The Golden Goblet",
                "The Weary Traveler",
                "The Drunken Dragon",
                "The Silver Stag",
                "The Rusty Anchor",
                "The Laughing Dwarf",
                "The Moonlit Inn"
            ]
        }
        
        for rel_path, contents in sample_tables.items():
            file_path = self.tables_dir / rel_path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            if not file_path.exists():
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(contents))
    
    def get_table_stats(self) -> Dict[str, int]:
        """Get statistics about loaded tables"""
        stats = {
            'total_categories': len(self.tables),
            'total_tables': sum(len(tables) for tables in self.tables.values()),
            'total_entries': sum(len(table) for category in self.tables.values() 
                               for table in category.values())
        }
        return stats
    
    def search_tables(self, search_term: str) -> List[Tuple[str, str, List[str]]]:
        """Search for tables containing the search term"""
        results = []
        search_term = search_term.lower()
        
        for category, tables in self.tables.items():
            for table_name, table_contents in tables.items():
                if search_term in table_name.lower():
                    results.append((category, table_name, table_contents))
                else:
                    # Search within table contents
                    matching_entries = [entry for entry in table_contents 
                                      if search_term in entry.lower()]
                    if matching_entries:
                        results.append((category, table_name, matching_entries))
        
        return results


class D100RollerApp:
    """Main application class with clean minimal design"""
    
    def __init__(self, root):
        self.root = root
        
        # Configure root window
        self.root.title("D100 Table Roller")
        self.root.geometry("1300x800")
        self.root.minsize(1000, 700)
        self.root.configure(bg='#f8f8f8')
        
        # Center window on screen
        self.center_window()
        
        # Initialize table manager
        self.table_manager = TableManager()
        
        # Current selections
        self.current_category = None
        self.current_table = None
        self.current_table_data = None
        
        # Roll mode tracking
        self.roll_mode = tk.StringVar(value="random")
        
        # Setup GUI
        self.setup_styles()
        self.create_widgets()
        self.setup_bindings()
        
        # Load initial data
        self.refresh_tables()
        
        # Create sample tables if none exist
        if not self.table_manager.tables:
            self.table_manager.create_sample_tables()
            self.refresh_tables()
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1300
        window_height = 800
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    def setup_styles(self):
        """Configure clean minimal styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Clean button styles
        style.configure('Accent.TButton', 
                       font=('Segoe UI', 9, 'bold'),
                       padding=(10, 6),
                       relief='solid',
                       borderwidth=1,
                       background='#007acc',
                       foreground='white')
        
        style.map('Accent.TButton',
                 background=[('active', '#005a9e')])
        
        style.configure('TButton', 
                       font=('Segoe UI', 9),
                       padding=(8, 4),
                       relief='solid',
                       borderwidth=1,
                       background='#f0f0f0',
                       foreground='#333333')
        
        style.map('TButton',
                 background=[('active', '#e0e0e0')])
        
        # Clean entry fields
        style.configure('TEntry', 
                       font=('Segoe UI', 9),
                       padding=4,
                       relief='solid',
                       borderwidth=1,
                       background='#f8f8f8')
        
        # Simple radio buttons
        style.configure('TRadiobutton', 
                       font=('Segoe UI', 9),
                       background='#f8f8f8',
                       foreground='#333333')
        
        # Clean treeview
        style.configure("Treeview", 
                       font=("Segoe UI", 9),
                       background='#f8f8f8',
                       fieldbackground='#f8f8f8',
                       borderwidth=1,
                       relief='solid')
        
        style.configure("Treeview.Heading", 
                       font=("Segoe UI", 9, "bold"),
                       background='#f0f0f0')
    
    def create_widgets(self):
        """Create clean minimal widgets"""
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#f8f8f8', padx=15, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎲 D100 Table Roller", 
                              font=('Segoe UI', 16, 'bold'),
                              bg='#f8f8f8', fg='#333333')
        title_label.pack(pady=(0, 15))
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg='#f8f8f8')
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Table browser
        left_frame = tk.Frame(content_frame, bg='#f8f8f8', relief='solid', bd=1)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10), pady=0)
        left_frame.pack_propagate(False)
        left_frame.configure(width=350)
        
        # Browser header
        browser_header = tk.Frame(left_frame, bg='#f8f8f8')
        browser_header.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(browser_header, text="Table Browser", 
                font=('Segoe UI', 10, 'bold'),
                bg='#f8f8f8', fg='#333333').pack(side=tk.LEFT)
        
        refresh_btn = ttk.Button(browser_header, text="↻", width=3,
                               command=self.refresh_tables)
        refresh_btn.pack(side=tk.RIGHT)
        
        # Search
        search_frame = tk.Frame(left_frame, bg='#f8f8f8')
        search_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(fill=tk.X)
        
        # Table tree
        tree_frame = tk.Frame(left_frame, bg='#f8f8f8')
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        self.tree = ttk.Treeview(tree_frame, show="tree")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        
        # File buttons
        file_frame = tk.Frame(left_frame, bg='#f8f8f8')
        file_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        ttk.Button(file_frame, text="Open Folder", 
                  command=self.open_tables_folder).pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(file_frame, text="Add Table", 
                  command=self.add_table_file).pack(side=tk.LEFT)
        
        # Right panel
        right_frame = tk.Frame(content_frame, bg='#f8f8f8')
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Table info
        info_frame = tk.Frame(right_frame, bg='#f8f8f8', relief='solid', bd=1)
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(info_frame, text="Table Information", 
                font=('Segoe UI', 10, 'bold'),
                bg='#f8f8f8', fg='#333333').pack(anchor=tk.W, padx=10, pady=(10, 5))
        
        self.table_name_label = tk.Label(info_frame, text="No table selected",
                                        bg='#f8f8f8', fg='#333333')
        self.table_name_label.pack(anchor=tk.W, padx=10)
        
        self.table_details_label = tk.Label(info_frame, text="",
                                           bg='#f8f8f8', fg='#666666')
        self.table_details_label.pack(anchor=tk.W, padx=10, pady=(0, 10))
        
        # Controls
        controls_frame = tk.Frame(right_frame, bg='#f8f8f8', relief='solid', bd=1)
        controls_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(controls_frame, text="Rolling Options", 
                font=('Segoe UI', 10, 'bold'),
                bg='#f8f8f8', fg='#333333').pack(anchor=tk.W, padx=10, pady=(10, 10))
        
        # Radio options in one row
        radio_frame = tk.Frame(controls_frame, bg='#f8f8f8')
        radio_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        ttk.Radiobutton(radio_frame, text="Random", variable=self.roll_mode, 
                       value="random", command=self.on_mode_change).pack(side=tk.LEFT, padx=(0, 15))
        
        specific_frame = tk.Frame(radio_frame, bg='#f8f8f8')
        specific_frame.pack(side=tk.LEFT, padx=(0, 15))
        
        ttk.Radiobutton(specific_frame, text="Specific:", variable=self.roll_mode, 
                       value="specific", command=self.on_mode_change).pack(side=tk.LEFT)
        
        self.specific_num_var = tk.StringVar()
        self.specific_entry = ttk.Entry(specific_frame, textvariable=self.specific_num_var,
                                       width=5)
        self.specific_entry.pack(side=tk.LEFT, padx=(5, 0))
        
        multiple_frame = tk.Frame(radio_frame, bg='#f8f8f8')
        multiple_frame.pack(side=tk.LEFT)
        
        ttk.Radiobutton(multiple_frame, text="Multiple:", variable=self.roll_mode, 
                       value="multiple", command=self.on_mode_change).pack(side=tk.LEFT)
        
        self.num_rolls_var = tk.StringVar(value="10")
        self.rolls_entry = ttk.Entry(multiple_frame, textvariable=self.num_rolls_var,
                                   width=5)
        self.rolls_entry.pack(side=tk.LEFT, padx=(5, 0))
        
        # Roll button
        button_frame = tk.Frame(controls_frame, bg='#f8f8f8')
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        self.roll_button = ttk.Button(button_frame, text="🎲 Roll", 
                                     command=self.roll_dice, style="Accent.TButton")
        self.roll_button.pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(button_frame, text="Clear", command=self.clear_results).pack(side=tk.LEFT)
        
        # Results
        results_frame = tk.Frame(right_frame, bg='#f8f8f8', relief='solid', bd=1)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(results_frame, text="Results", 
                font=('Segoe UI', 10, 'bold'),
                bg='#f8f8f8', fg='#333333').pack(anchor=tk.W, padx=10, pady=(10, 5))
        
        text_frame = tk.Frame(results_frame, bg='#f8f8f8')
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        self.results_text = tk.Text(text_frame, wrap=tk.WORD,
                                   font=("Segoe UI", 10),
                                   bg='#f8f8f8', fg='#333333',
                                   relief='flat', bd=0)
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        results_scroll = ttk.Scrollbar(text_frame, orient="vertical",
                                      command=self.results_text.yview)
        results_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_text.configure(yscrollcommand=results_scroll.set)
        
        # Initialize UI state
        self.update_ui_state()
    
    def setup_bindings(self):
        """Setup event bindings"""
        self.tree.bind("<<TreeviewSelect>>", self.on_table_select)
        self.search_var.trace("w", self.on_search_change)
        self.root.bind("<Return>", lambda e: self.roll_dice())
        
        vcmd = (self.root.register(self.validate_number), '%P')
        self.specific_entry.configure(validate='key', validatecommand=vcmd)
        self.rolls_entry.configure(validate='key', validatecommand=vcmd)
    
    def validate_number(self, value):
        """Validate numeric input"""
        if value == "":
            return True
        try:
            int(value)
            return True
        except ValueError:
            return False
    
    def on_mode_change(self):
        """Handle roll mode changes"""
        self.update_ui_state()
    
    def update_ui_state(self):
        """Update UI state based on current mode"""
        mode = self.roll_mode.get()
        
        if mode == "specific":
            self.specific_entry.configure(state='normal')
            self.rolls_entry.configure(state='disabled')
        elif mode == "multiple":
            self.specific_entry.configure(state='disabled')
            self.rolls_entry.configure(state='normal')
        else:  # random
            self.specific_entry.configure(state='disabled')
            self.rolls_entry.configure(state='disabled')
    
    def refresh_tables(self):
        """Refresh the table list"""
        self.table_manager.scan_tables()
        self.populate_tree()
    
    def populate_tree(self, filter_text=""):
        """Populate the tree with tables"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for category in self.table_manager.get_categories():
            category_id = self.tree.insert("", "end", text=f"📁 {category}")
            
            tables_added = 0
            for table_name in self.table_manager.get_tables_in_category(category):
                if not filter_text or filter_text.lower() in table_name.lower():
                    self.tree.insert(category_id, "end", text=f"📄 {table_name}",
                                   values=(category, table_name))
                    tables_added += 1
            
            if tables_added == 0 and filter_text:
                self.tree.delete(category_id)
        
        for item in self.tree.get_children():
            self.tree.item(item, open=True)
    
    def on_search_change(self, *args):
        """Handle search text changes"""
        filter_text = self.search_var.get()
        self.populate_tree(filter_text)
    
    def on_table_select(self, event):
        """Handle table selection"""
        selection = self.tree.selection()
        if not selection:
            return
        
        item = selection[0]
        values = self.tree.item(item, "values")
        
        if values:
            category, table_name = values
            self.current_category = category
            self.current_table = table_name
            self.current_table_data = self.table_manager.get_table(category, table_name)
            
            if self.current_table_data:
                self.table_name_label.config(text=table_name)
                self.table_details_label.config(text=f"{category} • {len(self.current_table_data)} entries")
                self.roll_button.config(state="normal")
            else:
                self.table_name_label.config(text="Error loading table")
                self.table_details_label.config(text="")
                self.roll_button.config(state="disabled")
        else:
            self.table_name_label.config(text="No table selected")
            self.table_details_label.config(text="")
            self.roll_button.config(state="disabled")
    
    def roll_dice_notation(self, text):
        """Process dice notation in text"""
        def replace_dice(match):
            dice_str = match.group(0)
            parts = dice_str.lower().split('d')
            if len(parts) == 2:
                try:
                    num_dice = int(parts[0])
                    die_size = int(parts[1])
                    total = sum(random.randint(1, die_size) for _ in range(num_dice))
                    return str(total)
                except ValueError:
                    return dice_str
            return dice_str
        
        dice_pattern = r'\b\d+[dD]\d+\b'
        return re.sub(dice_pattern, replace_dice, text)
    
    def roll_dice(self):
        """Roll the dice and display results"""
        if not self.current_table_data:
            messagebox.showwarning("No Table Selected", "Please select a table first!")
            return
        
        try:
            mode = self.roll_mode.get()
            results = []
            
            if mode == "specific":
                if not self.specific_num_var.get().strip():
                    messagebox.showerror("Invalid Input", "Please enter a specific number")
                    return
                    
                specific_num = int(self.specific_num_var.get())
                if specific_num < 1 or specific_num > len(self.current_table_data):
                    messagebox.showerror("Invalid Input", 
                                       f"Number must be between 1 and {len(self.current_table_data)}")
                    return
                
                result_text = self.current_table_data[specific_num - 1]
                results.append((specific_num, result_text))
                
            elif mode == "multiple":
                if not self.num_rolls_var.get().strip():
                    messagebox.showerror("Invalid Input", "Please enter number of rolls")
                    return
                    
                num_rolls = int(self.num_rolls_var.get())
                if num_rolls < 1 or num_rolls > 50:
                    messagebox.showerror("Invalid Input", "Number of rolls must be between 1 and 50")
                    return
                
                for _ in range(num_rolls):
                    roll = random.randint(1, len(self.current_table_data))
                    result_text = self.current_table_data[roll - 1]
                    results.append((roll, result_text))
            
            else:  # random mode
                roll = random.randint(1, len(self.current_table_data))
                result_text = self.current_table_data[roll - 1]
                results.append((roll, result_text))
            
            self.display_results(results)
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
    
    def display_results(self, results):
        """Display roll results cleanly"""
        self.results_text.delete(1.0, tk.END)
        
        self.results_text.insert(tk.END, f"🎲 {self.current_table}\n\n")
        
        for i, (roll, result) in enumerate(results, 1):
            processed_result = self.roll_dice_notation(result)
            
            if len(results) > 1:
                self.results_text.insert(tk.END, f"#{i:2d} [{roll:02d}] {processed_result}\n")
            else:
                self.results_text.insert(tk.END, f"[{roll:02d}] {processed_result}\n")
        
        self.results_text.see(tk.END)
    
    def clear_results(self):
        """Clear the results area"""
        self.results_text.delete(1.0, tk.END)
    
    def open_tables_folder(self):
        """Open the tables folder in file explorer"""
        tables_path = self.table_manager.tables_dir
        tables_path.mkdir(parents=True, exist_ok=True)
        
        import subprocess
        import sys
        
        try:
            if sys.platform == "win32":
                subprocess.run(["explorer", str(tables_path)])
            elif sys.platform == "darwin":
                subprocess.run(["open", str(tables_path)])
            else:
                subprocess.run(["xdg-open", str(tables_path)])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open folder: {e}")
    
    def add_table_file(self):
        """Add a new table file"""
        file_path = filedialog.askopenfilename(
            title="Select Table File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            import shutil
            src_path = Path(file_path)
            dest_path = self.table_manager.tables_dir / src_path.name
            
            try:
                shutil.copy2(src_path, dest_path)
                messagebox.showinfo("Success", f"Table file added: {src_path.name}")
                self.refresh_tables()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add table file: {e}")


def main():
    """Main entry point"""
    root = tk.Tk()
    
    try:
        root.iconbitmap("dice.ico")
    except:
        pass
    
    app = D100RollerApp(root)
    
    welcome_text = """🎲 Welcome to D100 Table Roller!

Select a table from the browser on the left and choose your rolling mode.
Click Roll to generate results.

The app supports dice notation (1d6, 2d8, etc.) in table entries."""
    
    app.results_text.insert(tk.END, welcome_text)
    
    root.mainloop()


if __name__ == "__main__":
    main()