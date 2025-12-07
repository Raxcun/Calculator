import tkinter as tk

def click_button(value):
    text_value = entry_var.get()
    entry_var.set(text_value + str(value))
def calculate():
    try:
        expression =  entry_var.get().replace('×', '*').replace('÷', '/').replace('^', '**').replace('%', '/100')
        result = eval(expression)
        entry_var.set(result)
    except:
        entry_var.set("Error")
def delete():
    entry_var.set(entry_var.get()[:-1])
def clear():
    entry_var.set("")



window = tk.Tk()
window.title('calculation')
window.minsize(width=300, height=400)

entry_var = tk.StringVar()
entry = tk.Entry(master=window, text=entry_var, font=("Arial", 20), justify="right", bd=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10, sticky="nsew")


buttons = [
    ('7', '8', '9', '<-'),
    ('4', '5', '6', 'C'),
    ('1', '2', '3', '-'),
    ('%', '0', '×', '÷'),
    ('.', '=','^', '+'),]

for row_index, row_values in enumerate(buttons, start=1):
    for col_index, value in enumerate(row_values):
        if value == "=":
            command = calculate
        elif value == "C":
            command = clear
        elif value == "<-":
            command = delete
        else:
            command = lambda v=value: click_button(v)
        button = tk.Button(window, text=value, font=("Arial", 16), width=5, height=2, bg="#F0F0F0", fg="black", relief="raised", command=command)
        button.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")

window.mainloop()
