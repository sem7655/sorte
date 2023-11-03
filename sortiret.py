import os
import shutil
import tkinter as tk
from tkinter import filedialog
# Устанави все библеотеки: pip install [name]
def sort_files(directory):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Documents": [".pdf", ".docx", ".txt"],
    }

    for dir_name in file_types:
        os.makedirs(os.path.join(directory, dir_name), exist_ok=True)
    for filename in os.listdir(directory):
        if filename != os.path.basename(__file__):
            src_path = os.path.join(directory, filename)

            for folder_name, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    dest_path = os.path.join(directory, folder_name, filename)
                    shutil.move(src_path, dest_path)
                    break
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        sort_files(directory)
        status_label.config(text=f"Files in {directory} are sorted.")

# GUI
root = tk.Tk()
root.title("File Sorter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

select_button = tk.Button(frame, text="Select Directory", command=select_directory)
select_button.pack(fill=tk.X)

status_label = tk.Label(frame, text="", pady=10)
status_label.pack(fill=tk.X)

root.mainloop()
