import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    for key, widget in entries.items():
        if key in required_fields:
            value = widget.get("1.0", tk.END).strip() if key == "Address" else widget.get().strip()
            if not value:
                messagebox.showerror("ААААААА ошибка", f"{key} обязательно к заполнению")
                return
    messagebox.showinfo("ура", "регистрация пройдена")

def reset_form():
    for key, widget in entries.items():
        if isinstance(widget, tk.Text):
            widget.delete("1.0", tk.END)
        else:
            widget.delete(0, tk.END)
            if isinstance(widget, ttk.Combobox):
                widget.set("Select")
    meal_pref.set("Vegetarian")
    for var in payment_vars.values():
        var.set(False)

# окно
root = tk.Tk()
root.title("Workshop Registration")
root.geometry("900x500")
entries = {}
required_fields = ["First Name", "Last Name", "Company/Institution", "Address", "Email"]

# шапка
header = tk.Frame(root, bg="#BFD6C9")
header.pack(fill=tk.X)
tk.Label(header, text="Workshop Registration", bg="#BFD6C9", font=("Arial", 16, "bold")).pack(side=tk.LEFT, padx=10,
                                                                                              pady=10)
tk.Label(header, text="More Actions ▼", bg="#BFD6C9", font=("Arial", 9, "bold")).pack(side=tk.LEFT, pady=10)
tk.Label(root, text="Register now while seats are available!", font=("Arial", 10, "underline")).pack(anchor=tk.W,
                                                                                                     padx=15)

# контейнер
form = tk.Frame(root)
form.pack(padx=15, pady=10)

left = tk.Frame(form)
left.grid(row=0, column=0, padx=10)
right = tk.Frame(form)
right.grid(row=0, column=1, padx=10, sticky="n")

# поля слева
fields = [
    "First Name", "Last Name", "Company/Institution", "Address",
    "City", "State / Province / Region", "Country", "Email", "Phone Number"
]

for field in fields:
    frame = tk.Frame(left)
    frame.pack(fill=tk.X, pady=3)
    tk.Label(frame, text=field + (" *" if field in required_fields else ""), width=25, anchor="w").pack(side=tk.LEFT)

    if field == "Address":
        widget = tk.Text(frame, height=4, width=35)
    elif "State" in field:
        widget = ttk.Combobox(frame, values=["Select"], state="readonly", width=30)
        widget.set("Select")
    elif "Country" in field:
        widget = ttk.Combobox(frame, values=["Select"], state="readonly", width=30)
        widget.set("Select")
    else:
        widget = ttk.Entry(frame, width=33)

    widget.pack(side=tk.LEFT)
    entries[field] = widget

# едааа
tk.Label(right, text="Lunch", font=("Arial", 10, "underline")).pack(anchor="w", pady=(0, 5))
tk.Label(right, text="Meal Preference").pack(anchor="w")

meal_pref = ttk.Combobox(right, values=["Vegetarian", "lalala", "bebebe"], state="readonly", width=25)
meal_pref.set("Vegetarian")
meal_pref.pack(anchor="w", pady=(0, 10))

# оплата
tk.Label(right, text="Payment Details", font=("Arial", 10, "underline")).pack(anchor="w")
tk.Label(right, text="Payment Mode").pack(anchor="w")

payment_vars = {}
for method in ["Cash", "Cheque", "Demand Draft"]:
    var = tk.BooleanVar()
    payment_vars[method] = var
    tk.Checkbutton(right, text=method, variable=var).pack(anchor="w")

# доп оплата
for label in ["DD/Cheque No.", "Drawn On (Bank Name)", "Payable at"]:
    frame = tk.Frame(right)
    frame.pack(fill=tk.X, pady=3)
    tk.Label(frame, text=label, width=20, anchor="w").pack(side=tk.LEFT)
    entry = ttk.Entry(frame, width=30)
    entry.pack(side=tk.LEFT)
    entries[label] = entry

# кнопки
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Submit", bg="#BFD6C9", padx=20, command=submit_form).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="Reset", bg="#BFD6C9", padx=20, command=reset_form).pack(side=tk.LEFT)

root.mainloop()