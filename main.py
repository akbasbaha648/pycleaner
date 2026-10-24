import tkinter as tk
import os
from tkinter import messagebox

def clean():
    os.system('rd /s /q "%TEMP%" & md "%TEMP%"')
    os.system('rd /s /q "%TEMP%" & md "%TEMP%"')
    messagebox.showinfo("successful", "unnecessary files cleaned")

root = tk.Tk()
root.title("PyCleaner v1.0.0")
root.geometry("600x600")
root.configure(bg="#87CEEB")

header = tk.Label(text="PyCleaner v1.0.0", font=("Default", 24), bg="#87CEEB")
header.pack(pady=5)

button1 = tk.Button(text="Clean", bg="#87CEEB", font=("Default", 16), fg="black", command=clean)
button1.pack()

root.mainloop()