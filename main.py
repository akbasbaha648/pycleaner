import tkinter as tk
import os
from tkinter import messagebox

def clean():
    os.system('rd /s /q "%TEMP%" & md "%TEMP%"')
    os.system('rd /s /q "C:/Windows/Temp" & md "C:/Windows/Temp"')
    messagebox.showinfo("Successful", "Temp Files Cleaned")

def analyze():
    analyzeResult = os.popen('wmic logicaldisk get deviceid, volumename, size, freespace').read()
    messagebox.showinfo("Analyzed", analyzeResult)

root = tk.Tk()
root.title("PyCleaner v1.0.1")
root.geometry("600x600")
root.configure(bg="#87CEEB")

header = tk.Label(text="PyCleaner v1.0.1", font=("Default", 24), bg="#87CEEB")
header.pack(pady=5)

button1 = tk.Button(text="Clean", bg="#87CEEB", font=("Default", 16), fg="black", command=clean)
button1.pack(pady=5)

button2= tk.Button(text="Analyze", bg="#87CEEB", font=("Default", 16), fg="black", command=analyze)
button2.pack(pady=5)

root.mainloop()
