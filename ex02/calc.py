import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = int(btn["text"])
    tkm.showinfo(f"{num}", f"{num}のボタンが押されました")

root = tk.Tk()
root.geometry("300x500")

r ,c = 0, 0
for i, num in enumerate(range(9,-1,-1), 1):
    btn = tk.Button(root, font = ("Times New Roman",30), text = f"{num}",width = 4, height = 2)
    btn.grid(row=r, column = c)
    btn.bind("<1>", click_number)
    c+=1
    if i %3 ==0:
        r += 1
        c = 0
    

root.mainloop()