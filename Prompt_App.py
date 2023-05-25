import tkinter as tk
import random
from tkinter import filedialog
from tkinter import messagebox
import os
import sys


# Pre-define the empty lists for each category:
pairings = []
locations = []
alt_universe = []
characters = []
fandoms = []
tags = []

# Ask the user if they want to use their own lists or the default lists:
def select_files():
    global pairing_filename, location_filename, alt_universe_filename, character_filename, fandom_filename, tags_filename
    if messagebox.askyesno(title="Custom Lists", message="Do you want to use your own source lists? \r\n\r\nThese are lists you will use for fandoms, pairings, AUs, locations, tags, and characters. They must be in .txt format. \r\n\r\nIf you choose No then the default files downloaded with this prompt app will be used.\r\n\r\nYou can choose to just use some of your own .txt files. For any sections where you want to use the default list, press Cancel on the file window."):
        # If they say yes, ask them for the filenames:
        fandom_filename = filedialog.askopenfilename(title="Select Fandoms List", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        pairing_filename = filedialog.askopenfilename(title="Select Pairings List", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        location_filename = filedialog.askopenfilename(title="Select Locations List", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        alt_universe_filename = filedialog.askopenfilename(title="Select AU List", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        character_filename = filedialog.askopenfilename(title="Select Characters List", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        tags_filename = filedialog.askopenfilename(title="Select Tags List", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    else:
        # If they say no, use the default filenames:
        pairing_filename = 'pairings.txt'
        location_filename = 'locations.txt'
        alt_universe_filename = 'alternate_universe.txt'
        character_filename = 'characters.txt'
        fandom_filename = 'fandoms.txt'
        tags_filename = 'tags.txt'

    # If the user didn't select a file, or the file doesn't exist, use the default filename:
    if not pairing_filename or not os.path.isfile(pairing_filename):
        pairing_filename = 'pairings.txt'
    if not location_filename or not os.path.isfile(location_filename):
        location_filename = 'locations.txt'
    if not alt_universe_filename or not os.path.isfile(alt_universe_filename):
        alt_universe_filename = 'alternate_universe.txt'    
    if not character_filename or not os.path.isfile(character_filename):
        character_filename = 'characters.txt'
    if not fandom_filename or not os.path.isfile(fandom_filename):
        fandom_filename = 'fandoms.txt'    
    if not tags_filename or not os.path.isfile(tags_filename):
        tags_filename = 'tags.txt'


#Define the button functions:
def clear_prompts():
    pairing_var.set('')
    location_var.set('')
    alt_universe_var.set('')
    fandom_var.set('')
    fandom_crossover_var.set('')
    character_a_var.set('')
    character_b_var.set('')
    tag_one_var.set('')
    tag_two_var.set('')
    tag_three_var.set('')

# File Path location (for packaging as a .exe)
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def generate_pairing():
    try:
        with open(resource_path(pairing_filename), 'r') as file:
            pairings = file.readlines()
            pairings = [pairing.strip() for pairing in pairings]
            if not pairings:
                messagebox.showerror("Error", "Pairings list is empty.")
                return
        pairing_var.set(random.choice(pairings))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")
        
def generate_fandom():
    try:
        with open(resource_path(fandom_filename), 'r') as file:
            fandoms = file.readlines()
            fandoms = [fandom.strip() for fandom in fandoms]
            if not fandoms:
                messagebox.showerror("Error", "Fandoms list is empty.")
                return
        fandom_var.set(random.choice(fandoms))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")
        
def generate_crossover_fandom():
    try:
        with open(resource_path(fandom_filename), 'r') as file:
            fandoms = file.readlines()
            fandoms = [fandom.strip() for fandom in fandoms]
            if not fandoms:
                messagebox.showerror("Error", "Fandoms list is empty.")
                return
        fandom_crossover_var.set(random.choice(fandoms))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")

def generate_location():
    try:
        with open(resource_path(location_filename), 'r', encoding='utf-8') as file:
            locations = file.readlines()
            locations = [location.strip() for location in locations]
            if not locations:
                messagebox.showerror("Error", "Locations list is empty.")
                return
        location_var.set(random.choice(locations))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")

def generate_alt_universe():
    try:
        with open(resource_path(alt_universe_filename), 'r') as file:
            alt_universes = file.readlines()
            alt_universes = [alt_universe.strip() for alt_universe in alt_universes]
            if not alt_universes:
                messagebox.showerror("Error", "AU list is empty.")
                return
        alt_universe_var.set(random.choice(alt_universes))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")
        
def generate_character_a():
    try:
        with open(resource_path(character_filename), 'r') as file:
            characters = file.readlines()
            characters = [character.strip() for character in characters]
            if not characters:
                messagebox.showerror("Error", "Characters list is empty.")
        character_a_var.set(random.choice(characters))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")

def generate_character_b():
    try:
        with open(resource_path(character_filename), 'r') as file:
            characters = file.readlines()
            characters = [character.strip() for character in characters]
            if not characters:
                messagebox.showerror("Error", "Characters list is empty.")
        character_b_var.set(random.choice(characters))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")
        
def generate_tag_one():
    try:
        with open(resource_path(tags_filename), 'r') as file:
            tags = file.readlines()
            tags = [tag.strip() for tag in tags]
            if not tags:
                messagebox.showerror("Error", "Tags list is empty.")
        tag_one_var.set(random.choice(tags))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")
        
def generate_tag_two():
    try:
        with open(resource_path(tags_filename), 'r') as file:
            tags = file.readlines()
            tags = [tag.strip() for tag in tags]
            if not tags:
                messagebox.showerror("Error", "Tags list is empty.")
        tag_two_var.set(random.choice(tags))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")

def generate_tag_three():
    try:
        with open(resource_path(tags_filename), 'r') as file:
            tags = file.readlines()
            tags = [tag.strip() for tag in tags]
            if not tags:
                messagebox.showerror("Error", "Tags list is empty.")
        tag_three_var.set(random.choice(tags))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")

# Build the window and canvas within to allow for scrollbar
# Create a window:
window = tk.Tk()
window.title("Random Prompt Generator")
window.geometry("650x650")
window.configure(bg='#fdf8ff')

# Create a canvas for scrolling
canvas = tk.Canvas(window, bg='#fdf8ff', highlightthickness=0) 
canvas.pack(side="left", fill="both", expand=True, padx=60)

# Add a scrollbar to the canvas
scrollbar = tk.Scrollbar(window, command=canvas.yview)
scrollbar.pack(side="left", fill="y")

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Enable mousewheel scrolling
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)
canvas.bind("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))
canvas.bind("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))

# Create a frame to contain everything and add it to the canvas:
main_frame = tk.Frame(canvas, bg='#fdf8ff')
canvas.create_window((0, 0), window=main_frame, anchor="nw")

# Create a label for the title and place it at the top of main_frame
title_label = tk.Label(main_frame, text="Fanwork Prompt Generator", font=("Helvetica", 24, "bold"), bg='#fdf8ff')
title_label.pack(pady=30)

# Create a label for the subtitle and place it at the top of main_frame under the title
subtitle_label = tk.Label(main_frame, text="Use as many or as few prompts as you want. \nPress 'Clear' in the bottom right to start again.", font=("Helvetica", 16), bg='#fdf8ff')
subtitle_label.pack(pady=15)

# Create textvariables for each output box:
pairing_var = tk.StringVar()
fandom_var = tk.StringVar()
fandom_crossover_var = tk.StringVar()
location_var = tk.StringVar()
alt_universe_var = tk.StringVar()
character_a_var = tk.StringVar()
character_b_var = tk.StringVar()
tag_one_var = tk.StringVar()
tag_two_var = tk.StringVar()
tag_three_var = tk.StringVar()

# Create frames to hold the left and right sections of the window:
left_frame = tk.Frame(main_frame, bg='#fdf8ff')
right_frame = tk.Frame(main_frame, bg='#fdf8ff')
left_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_columnconfigure(0, weight=1)
left_frame.pack(side="left", expand=True, fill="both", padx=10)
right_frame.pack(side="right", expand=True, fill="both", padx=10)

# Create the labels, buttons, and output boxes for the left side:
fandom_label = tk.Label(left_frame, text="Fandom", bg='#fdf8ff', font=("Helvetica", 14, "bold"))
fandom_label.grid(pady=10, row=0, column=0)
fandom_button = tk.Button(left_frame, text="Generate Fandom", command=generate_fandom, borderwidth=2, relief="raised", bg='#880303', fg='#ffffff', font=("Helvetica", 10, "bold"))
fandom_button.grid(pady=10, row=1, column=0)
fandom_output = tk.Label(left_frame, textvariable=fandom_var, bg='#fdf8ff', wraplength=200, justify="left", font=("Helvetica", 14))
fandom_output.grid(pady=10, row=2, column=0)

fandom_crossover_label = tk.Label(left_frame, text="Fandom Crossover", bg='#fdf8ff', font=("Helvetica", 14, "bold"))
fandom_crossover_label.grid(pady=10, row=3, column=0)
fandom_crossover_button = tk.Button(left_frame, text="Generate Crossover Fandom", command=generate_crossover_fandom, borderwidth=2, relief="raised", bg='#880303', fg='#ffffff', font=("Helvetica", 10, "bold"))
fandom_crossover_button.grid(pady=10, row=4, column=0)
fandom_crossover_output = tk.Label(left_frame, textvariable=fandom_crossover_var, bg='#fdf8ff', wraplength=200, justify="left", font=("Helvetica", 14))
fandom_crossover_output.grid(pady=10, row=5, column=0)

pairing_label = tk.Label(left_frame, text="Pairing", bg='#fdf8ff', font=("Helvetica", 14, "bold"))
pairing_label.grid(pady=10, row=6, column=0)
pairing_button = tk.Button(left_frame, text="Generate Pairing", command=generate_pairing, borderwidth=2, relief="raised", bg='#880303', fg='#ffffff', font=("Helvetica", 10, "bold"))
pairing_button.grid(pady=10, row=7, column=0)
pairing_output = tk.Label(left_frame, textvariable=pairing_var, bg='#fdf8ff', wraplength=200, justify="left", font=("Helvetica", 14))
pairing_output.grid(pady=10, row=8, column=0)

location_label = tk.Label(left_frame, text="Location", bg='#fdf8ff', font=("Helvetica", 14, "bold"))
location_label.grid(pady=10, row=9, column=0)
location_button = tk.Button(left_frame, text="Generate Location", command=generate_location, borderwidth=2, relief="raised", bg='#880303', fg='#ffffff', font=("Helvetica", 10, "bold"))
location_button.grid(pady=10, row=10, column=0)
location_output = tk.Label(left_frame, textvariable=location_var, bg='#fdf8ff', wraplength=200, justify="left", font=("Helvetica", 14))
location_output.grid(pady=10, row=11, column=0)

alt_universe_label = tk.Label(left_frame, text="AU", bg='#fdf8ff', font=("Helvetica", 14, "bold"))
alt_universe_label.grid(pady=10, row=12, column=0)
alt_universe_button = tk.Button(left_frame, text="Generate AU", command=generate_alt_universe, borderwidth=2, relief="raised", bg='#880303', fg='#ffffff', font=("Helvetica", 10, "bold"))
alt_universe_button.grid(pady=10, row=13, column=0)
alt_universe_output = tk.Label(left_frame, textvariable=alt_universe_var, bg='#fdf8ff', wraplength=200, justify="left", font=("Helvetica", 14))
alt_universe_output.grid(pady=10, row=14, column=0)

# Create the labels, buttons, and output boxes for the right side:

character_a_label = tk.Label(right_frame, text="Character A", bg='#fdf8ff', font=("Helvetica", 14, "bold"))
character_a_label.grid(pady=10, row=3, column=0)
character_a_button = tk.Button(right_frame, text="Generate Character", command=generate_character_a, borderwidth=2, relief="raised", bg='#880303', fg='#ffffff', font=("Helvetica", 10, "bold"))
character_a_button.grid(pady=10, row=4, column=0)
character_a_output = tk.Label(right_frame, textvariable=character_a_var, bg='#fdf8ff', wraplength=200, justify="left", font=("Helvetica", 14))
character_a_output.grid(pady=10, row=5, column=0)

character_b_label = tk.Label(right_frame, text="Character B", bg='#fdf8ff', font=("Helvetica", 14, "bold"))
character_b_label.grid(pady=10, row=6, column=0)
character_b_button = tk.Button(right_frame, text="Generate Character", command=generate_character_b, borderwidth=2, relief="raised", bg='#880303', fg='#ffffff', font=("Helvetica", 10, "bold"))
character_b_button.grid(pady=10, row=7, column=0)
character_b_output = tk.Label(right_frame, textvariable=character_b_var, bg='#fdf8ff', wraplength=200, justify="left", font=("Helvetica", 14))
character_b_output.grid(pady=10, row=8, column=0)

tag_one_label = tk.Label(right_frame, text="Tag 1", bg='#fdf8ff', font=("Helvetica", 14, "bold"))
tag_one_label.grid(pady=10, row=9, column=0)
tag_one_button = tk.Button(right_frame, text="Generate Tag 1", command=generate_tag_one, borderwidth=2, relief="raised", bg='#880303', fg='#ffffff', font=("Helvetica", 10, "bold"))
tag_one_button.grid(pady=10, row=10, column=0)
tag_one_output = tk.Label(right_frame, textvariable=tag_one_var, bg='#fdf8ff', wraplength=200, justify="left", font=("Helvetica", 14))
tag_one_output.grid(pady=10, row=11, column=0)

tag_one_label = tk.Label(right_frame, text="Tag 2", bg='#fdf8ff', font=("Helvetica", 14, "bold"))
tag_one_label.grid(pady=10, row=12, column=0)
tag_one_button = tk.Button(right_frame, text="Generate Tag 2", command=generate_tag_two, borderwidth=2, relief="raised", bg='#880303', fg='#ffffff', font=("Helvetica", 10, "bold"))
tag_one_button.grid(pady=10, row=13, column=0)
tag_one_output = tk.Label(right_frame, textvariable=tag_two_var, bg='#fdf8ff', wraplength=200, justify="left", font=("Helvetica", 14))
tag_one_output.grid(pady=10, row=14, column=0)

tag_one_label = tk.Label(right_frame, text="Tag 3", bg='#fdf8ff', font=("Helvetica", 14, "bold"))
tag_one_label.grid(pady=10, row=15, column=0)
tag_one_button = tk.Button(right_frame, text="Generate Tag 3", command=generate_tag_three, borderwidth=2, relief="raised", bg='#880303', fg='#ffffff', font=("Helvetica", 10, "bold"))
tag_one_button.grid(pady=10, row=16, column=0)
tag_one_output = tk.Label(right_frame, textvariable=tag_three_var, bg='#fdf8ff', wraplength=200, justify="left", font=("Helvetica", 14))
tag_one_output.grid(pady=10, row=17, column=0)

clear_button = tk.Button(right_frame, text="   Clear   ", command=clear_prompts, borderwidth=3, relief="ridge", bg='#328fff', fg='#ffffff', font=("Helvetica", 10, "bold"))
clear_button.grid(pady=10, row=19, column=0)

select_files()

# Start the event loop:
window.mainloop()
