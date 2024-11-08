from tkinter import * # Testing new SSH github key
from customtkinter import *
from pathlib import Path
from PIL import ImageTk, Image
# After I finish this build, I want to watch that tutorial from.... 
# Atlas! the video on YT is called "Using tkinter with Classes" so I can convert this to a class based app

# Allow theme switch
def change_theme():
    if app._theme_name == "light":
        app._set_appearance_mode("dark")
    else:
        app._set_appearance_mode("light")
# get the height and width of resized box

def btn_mouse(event, btn, color):
    btn.configure(fg_color = color)
    btn.configure(text_color = light_color)

def save_file(event, button, color):
    # Get the filename by opening a filedialog from the default tkinter library
    # Use the btn_mouse function here to change the color when clicked so it's different than when you hover with the mouse
    file_name = filedialog.asksaveasfilename(defaultextension = ".txt", filetypes = [("Text Files", "*.txt"),("Python Files", "*.py"),("All Files", "*.*")])

    if file_name: # If a file name was provided
        button.configure(fg_color = color)
        file_string = field.get("1.0", END).strip() # Get ALL text from start "1.0" to finish END, and strip off any newline characters

        with open(file_name, "w") as f:
            for line in file_string:
                f.write(line)
        app.update_idletasks()
        button.configure(fg_color = color)
        button.configure(text_color = dark_color)
        print(f"Text written to file: {file_name}")
    else:
        print(f"File name was not given!")
def save_backup(file_string):
    with open("backup.txt", "w") as save_backup:
        save_backup.write(file_string)
    print("Replaced the Backup file with last entry!")

def load_file(event, button, color):
    file_name = filedialog.askopenfilename(defaultextension = ".txt", filetypes = [("Text Files", "*.txt"),("Python Files", "*.py"),("All Files", "*.*")])

    if file_name:
        button.configure(fg_color = color)
        
        with open(file_name, "r") as f:
            text = f.read()
            

        save_backup(field.get("1.0", END).strip())
        field.delete("1.0", END)
        field.insert("1.0", text)

def load_backup(event):
    with open("backup.txt", "r") as backup:
        text = backup.read()

    field.insert("1.0", text)

def new_file(event, button, color):
    old_text = field.get("1.0", END).strip()
    save_backup(old_text)
    button.configure(fg_color = color)
    field.delete("1.0", END)



# Define the Journal
title = "Journal"
default_width = 900
default_height = 600
current_w = default_width
current_h = default_height
app = CTk()
app.title(title)
app.geometry(f"{default_width}x{default_height}")
app.grid_columnconfigure(0, weight = 1)
app.grid_rowconfigure(1, weight = 1)

# Icon
root_path = Path(__file__).parent
icon_path = str(root_path / "icon-small-windows-version.ico")
print(icon_path)

try: 
    
    # icon_image = ImageTk.PhotoImage(Image.open(icon_path))
    icon_windows_image = app.wm_iconbitmap(icon_path)
    app.iconphoto(False, icon_windows_image)
    # Calls the resize function everytime I resize the window,
    # the "bind" method forces an event in this case "Configure" to a function
except Exception as E:
    print(f"Icon could not load: {E}")
    

code_font = ("Consolas", 20)
dark_color = "#1D2231"
header_color = "#2a2332"
button_color = "#342f47"
button_highlight_color = "#54426b"
button_click_color = "#A68DAD"
light_color = "#D1E2D1"


# Header 
header = CTkFrame(app, 
                  width = current_w, 
                  height = 50, 
                  fg_color = header_color, 
                  corner_radius = 0)

header.grid(column = 0, row = 0, sticky = "ew")

# Save Button


save_button = CTkButton(master = header, 
                        text = "Save", 
                        width = 75, 
                        height = 40, 
                        fg_color = button_color, 
                        text_color=light_color, 
                        hover = button_highlight_color, 
                        corner_radius = 5)
# Binding some functions...
save_button.grid(column = 0, row = 1, pady = 5, padx = 5)
save_button.bind("<Enter>", lambda event: btn_mouse("<Enter>", save_button, button_highlight_color))
save_button.bind("<Leave>", lambda event: btn_mouse("<Leave>", save_button, button_color))
save_button.bind("<Button-1>", lambda event: save_file(event = "<Button-1>", button = save_button, color = button_click_color))

# Load Button
load_button = CTkButton(master = header, 
                        text = "Load", 
                        width = 75, 
                        height = 40, 
                        fg_color = button_color,
                        hover = button_highlight_color,
                        corner_radius= 5)

load_button.grid(column = 1, row = 1, pady = 5, padx = 5)
load_button.bind("<Enter>", lambda event: btn_mouse("<Enter>", load_button, button_highlight_color))
load_button.bind("<Leave>", lambda event: btn_mouse("<Leave>", load_button, button_color))
load_button.bind("<Button-1>", lambda event: load_file(event = "<Button-1>", button = load_button, color = button_click_color))

# New Button
new_button = CTkButton(master = header,
                       text = "New File",
                       width = 75,
                       height = 40,
                       fg_color = button_color,
                       hover = button_highlight_color,
                       corner_radius = 5)

new_button.grid(column = 2, row = 1, pady = 5, padx = 5)
new_button.bind("<Enter>", lambda event: btn_mouse("<Enter>", new_button, button_highlight_color))
new_button.bind("<Leave>", lambda event: btn_mouse("<Leave>", new_button, button_color))
new_button.bind("<Button-1>", lambda event: new_file(event = "<Button-1>", button = new_button, color = button_click_color))


# Make the text box
field = CTkTextbox(app,
                    width = (current_w - 100),
                    height = current_h,
                    corner_radius = 5,
                    bg_color = (light_color, dark_color), 
                    font = code_font,
                    text_color=light_color)

field.grid(column = 0, row = 1, sticky = "nsew")
field.grid_rowconfigure(1, weight = 1)

# Load in the last text file from backup.txt
load_backup(event = "<Visibility>")
app.mainloop()