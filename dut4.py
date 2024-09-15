import os
import shutil
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font as tkfont
import hashlib


# Backend routine for copying files
def autoupload(src_dir, dst_dir):
    try:
        # Check if source directory is empty
        if not os.listdir(src_dir):
            messagebox.showinfo("Info", "Source directory is empty.")
            return
        dir_list = os.listdir(src_dir)
        total_files = len(dir_list)
        progress_bar['maximum'] = total_files

        for index, filename in enumerate(dir_list):
            src_path = os.path.join(src_dir, filename)
            dst_path = os.path.join(dst_dir, filename)
            # Ensure we only copy files, not directories
            if os.path.isfile(src_path):
                # Copy the file
                start = time.time()
                shutil.copyfile(src_path, dst_path)
                end = time.time()
                time_taken = end - start
                print(f"Time taken to copy file: {time_taken:.2f} seconds")
                start = time.time()
                # Verify checksum
                src_checksum = md5_checksum(src_path)
                dst_checksum = md5_checksum(dst_path)
                if src_checksum and dst_checksum and src_checksum != dst_checksum:
                    messagebox.showwarning("Warning", f"Checksum mismatch for file {filename}.")
                else:
                    print(f"Copied file {filename} from {src_path} to {dst_path}")
                end = time.time()
                time_taken = end - start
                print(f"Checksum done in: {time_taken:.2f} seconds")
            # Update progress bar
            progress_bar['value'] = index + 1
            root.update_idletasks()  # Ensure the progress bar is updated immediately
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
#backend routine for MD5 checksum
def md5_checksum(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to calculate checksum for {file_path}: {e}")
        return None
    return hash_md5.hexdigest()

# Frontend routine
def get_links():
    source_dir = entry_url1.get().strip()
    destination_dir = entry_url2.get().strip()
    destination_dir1 = entry_url3.get().strip()
    destination_dir2 = entry_url4.get().strip()

    if not os.path.isdir(source_dir):
        messagebox.showerror("Error", "The source directory does not exist.")
        return

    if not os.path.isdir(destination_dir):
        if not os.path.isdir(destination_dir1):
            if not os.path.isdir(destination_dir2):
                messagebox.showerror("Error", "The destination directory does not exist.")
                return

    # Reset the progress bar before starting
    progress_bar['value'] = 0
    if os.path.isdir(destination_dir):
        autoupload(source_dir, destination_dir)
    if os.path.isdir(destination_dir1):
        autoupload(source_dir, destination_dir1)
    if os.path.isdir(destination_dir2):
        autoupload(source_dir, destination_dir2)
    messagebox.showinfo("Success", f"Autoupload finished successfully.")

# Create the main application window
root = tk.Tk()
root.title("Carlos Autouploader")
#root.iconbitmap("carlos.ico")

# Define fonts
title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
label_font = tkfont.Font(family="Arial", size=12)
button_font = tkfont.Font(family="Arial", size=12, weight="bold")

# Set a background color
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Directory Copy Utility 4", font=title_font, bg="#f0f0f0")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Source Directory Label and Entry
tk.Label(root, text="Enter source directory:", font=label_font, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10,
                                                                                   sticky='e')
entry_url1 = tk.Entry(root, width=50, font=label_font)
entry_url1.grid(row=1, column=1, padx=10, pady=10)

# Destination Directory Label and Entry
tk.Label(root, text="Enter destination directory:", font=label_font, bg="#f0f0f0").grid(row=2, column=0, padx=10,
                                                                                        pady=10, sticky='e')
entry_url2 = tk.Entry(root, width=50, font=label_font)
entry_url2.grid(row=2, column=1, padx=10, pady=10)

# Destination Directory 2 Label and Entry
tk.Label(root, text="Enter destination directory 2:", font=label_font, bg="#f0f0f0").grid(row=3, column=0, padx=10,
                                                                                        pady=10, sticky='e')
entry_url3 = tk.Entry(root, width=50, font=label_font)
entry_url3.grid(row=3, column=1, padx=10, pady=10)

# Destination Directory 3 Label and Entry
tk.Label(root, text="Enter destination directory 3:", font=label_font, bg="#f0f0f0").grid(row=4, column=0, padx=10,
                                                                                        pady=10, sticky='e')
entry_url4 = tk.Entry(root, width=50, font=label_font)
entry_url4.grid(row=4, column=1, padx=10, pady=10)

# Execute Button
execute_button = tk.Button(root, text="Autoupload 4", command=get_links, font=button_font, bg="#4CAF50", fg="white",
                           relief="raised", padx=10, pady=5)
execute_button.grid(row=5, columnspan=2, pady=20)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
# Set window size and position
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = ((screen_width - window_width) // 2)-610  # Center horizontally
y = (screen_height - window_height) -80  # Center vertically
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
# Run the Tkinter event loop
root.mainloop()
