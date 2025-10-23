import tkinter as tk

#Main Window
root = tk.Tk()
root.title("My Calculator")

#input/output
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=3, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, pady=10)

#Button Function
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

#Button
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

# Create buttons dynamically
row_val = 1
col_val = 0
for btn_text in buttons:
    button = tk.Button(root, text=btn_text, font=("Arial", 18), padx=20, pady=10)
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
