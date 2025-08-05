#This is the script that starts the gui
from tkinter import *
import tkinter as tk
from tkinter import ttk
import subprocess

sourcelist = {}
file_path = "sourcelist.txt"

def update_sources():
    try:
        with open(file_path) as file:
            for line in file:
                line = line.strip()
                try:
                    path, index = line.split()
                    sourcelist[path] = index
                except ValueError:
                    x = line
                    y = ''
    except FileNotFoundError:
        print(f"Error: the file: {file_path} was not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
    combobox_values = list(sourcelist.keys())
    return combobox_values

#select event
def on_select(event):
    #update_sources()
    print("item was selected")
    selected_key = combo_box.get()
    value = sourcelist.get(selected_key)
    print(f"Selected: {selected_key}, Value: {value}")
    subprocess.run(['python', 'video_player.py', selected_key, value])

#all local button click event
def on_all_local_click():
    print("all local was clicked")
    subprocess.run(['python', 'play_all_local.py'])

#source entry button
def on_source_entry_click():
    try:
        with open(file_path, "a") as file:
            file.write(source_entry.get() + " 0\n")
    except FileNotFoundError:
        print(f"Error: the file: {file_path} was not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
    print(f"adding: {source_entry.get()} to source list")
    combo_box['values'] = update_sources()
    source_entry.delete(0, tk.END)

#source entry button
def on_source_remove_click():
    target_line = removal_entry.get() + " 0"
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()  # Read all lines into a list

        with open(file_path, "w") as f:
            for line in lines:
                if line.strip() != target_line:  # Check if the line matches (strip() removes newline)
                    f.write(line)
        print(f"Line '{target_line}' removed from {file_path}")
        combo_box['values'] = update_sources()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    
    
    removal_entry.delete(0, tk.END)
   
#build the gui components
root = tk.Tk()
root.title("Video Source Selection")
root.geometry("670x250+1220+50")
root.configure(bg = "slategray")

#frames
frame_selection = tk.Frame(borderwidth=2, relief="solid")
frame_selection.place(x=16, y=15, width=300, height=75)

frame_add = tk.Frame(borderwidth=2, relief="solid", bg= "light grey")
frame_add.place(x=16, y=115, width=300, height=80)

frame_remove = tk.Frame(borderwidth=2, relief="solid")
frame_remove.place(x=330, y=115, width=330, height=80)

frame_button = tk.Frame(borderwidth=2, relief="solid")
frame_button.place(x=390, y=20, width=182, height=62)

#source entry label
label_source_entry = Label(root,text="Enter a source to add to source list")
label_source_entry.place(x=25, y=120)

#source entry text
source_entry = ttk.Entry(root)
source_entry.place(x=25, y=150)

#source entry button
btn_source_entry = tk.Button(
    text = "Add Source",
    bg = "white",
    fg = "black",
    command = on_source_entry_click
)
btn_source_entry.place(x=205, y=150)

#label source removal
label_source_removal = Label(root,text="Enter a source to be removed")
label_source_removal.place(x=340, y=120)

#removal entry
removal_entry = ttk.Entry(root)
removal_entry.place(x=340, y=150)

#source remove button
btn_source_remove = tk.Button(
    text = "Remove Source",
    bg = "red3",
    fg = "black",
    command = on_source_remove_click
)
btn_source_remove.place(x=520, y=150)

#combobox label
label = Label(root,text="Select a source for video input")
label.place(x=25, y=25)

# #create the combobox
combo_box = ttk.Combobox(root,values=update_sources())
combo_box.set("Select Source")
combo_box.place(x=25,y=55, height=20, width=260)

#define play all local button
btn_play_all = tk.Button(
    text = "Play All Local Cameras",
    bg = "green",
    fg = "black",
    command = on_all_local_click
)

btn_play_all.place(x=390, y=20, height = 60, width = 180)

combo_box.bind("<<ComboboxSelected>>", on_select)
root.mainloop()