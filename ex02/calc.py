import tkinter as tk


root = tk.Tk()
root.geometry("300x500")

r ,c = 0, 0
for i, num in enumerate(range(9,-1,-1), 1):
    button = tk.Button(root, font = ("Times New Roman",30), text = f"{num}",width = 4, height = 2)
    button.grid(row=r, column = c)
    c+=1
    if i %3 ==0:
        r += 1
        c = 0
    

root.mainloop()