import tkinter as tk
from tkinter import ttk, messagebox
class FoodItem:
def __init__(self, name, price):
self.name = name
self.price = price
class Order:
def __init__(self):
self.items = []
def add_item(self, food_item):
self.items.append(food_item)
def remove_item(self, index):
del self.items[index]
def total_price(self):
return sum(item.price for item in self.items)
class OnlineFoodOrderingApp:
def __init__(self, master):
self.master = master
self.master.title("Online Food Ordering System")
self.master.geometry("800x600")
self.master.configure(bg="#3AAFA9")
self.style = ttk.Style()

8
self.style.theme_use('clam')
self.style.configure("TFrame", background="#3AAFA9")
self.style.configure("TLabel", background="#3AAFA9",
foreground="white")
self.style.configure("TButton", foreground="red", padding=(10, 5),
font=('Arial', 12))
self.style.map("TButton", background=[('active', '#16A085')])
self.food_items = [
FoodItem("Pizza", 10),
FoodItem("Burger", 5),
FoodItem("Sandwich", 7),
FoodItem("Fruit Drink", 3),
FoodItem("Cold Drink", 2),
]
self.order = Order()
self.create_widgets()
def create_widgets(self):
# Divide the window into sections
self.master.grid_rowconfigure(0, weight=1)
self.master.grid_rowconfigure(1, weight=1)
self.master.grid_columnconfigure(0, weight=1)
# Menu Frame
self.menu_frame = ttk.LabelFrame(self.master, text="Menu",
padding=(10, 10))
self.menu_frame.grid(row=0, column=0, padx=10, pady=10,
sticky="nsew")

9

# Order Frame
self.order_frame = ttk.LabelFrame(self.master, text="Your Order",
padding=(10, 10))
self.order_frame.grid(row=1, column=0, padx=10, pady=10,
sticky="nsew")
self.create_menu_widgets()
self.create_order_widgets()
# Quote Label
quote_text = "Good food is the foundation of genuine happiness. -
Auguste Escoffier"
self.quote_label = ttk.Label(self.master, text=quote_text, font=('Arial',
14), background="#3AAFA9", foreground="white")
self.quote_label.grid(row=1, column=0, padx=10, pady=(200, 0),
sticky="nsew")
# Centering the Quote Label
self.master.grid_rowconfigure(1, weight=1)
self.master.grid_columnconfigure(0, weight=1)
def create_menu_widgets(self):
for i, food_item in enumerate(self.food_items):
item_label = ttk.Label(self.menu_frame, text=f"{food_item.name}
- ${food_item.price}")
item_label.grid(row=i, column=0, sticky="w", pady=5)
add_button = ttk.Button(self.menu_frame, text="Add",
command=lambda idx=i: self.add_to_order(idx))
add_button.grid(row=i, column=1, padx=5, pady=5, sticky="e")
add_button.bind("<Enter>", lambda event, button=add_button:
self.on_enter(button))

10

add_button.bind("<Leave>", lambda event, button=add_button:
self.on_leave(button))
def create_order_widgets(self):
self.order_listbox = tk.Listbox(self.order_frame,
selectmode=tk.SINGLE, width=30, height=10, bg="#F0F0F0",
fg="#333333", font=('Arial', 12))
self.order_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll_bar = tk.Scrollbar(self.order_frame, orient=tk.VERTICAL,
command=self.order_listbox.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
self.order_listbox.config(yscrollcommand=scroll_bar.set)
remove_button = ttk.Button(self.order_frame, text="Remove",
command=self.remove_from_order)
remove_button.pack(pady=5, fill=tk.X)
remove_button.bind("<Enter>", lambda event, button=remove_button:
self.on_enter(button))
remove_button.bind("<Leave>", lambda event, button=remove_button:
self.on_leave(button))
self.total_label = ttk.Label(self.order_frame, text="Total: $0",
background="#F0F0F0", foreground="#333333", font=('Arial', 12))
self.total_label.pack(pady=5)
checkout_button = ttk.Button(self.order_frame, text="Checkout",
command=self.checkout)
checkout_button.pack(pady=5, fill=tk.X)
checkout_button.bind("<Enter>", lambda event,
button=checkout_button: self.on_enter(button))
checkout_button.bind("<Leave>", lambda event,

11

button=checkout_button: self.on_leave(button))
def add_to_order(self, index):
food_item = self.food_items[index]
self.order.add_item(food_item)
self.update_order_list()
self.update_total()
def remove_from_order(self):
selected_index = self.order_listbox.curselection()
if selected_index:
self.order.remove_item(selected_index[0])
self.update_order_list()
self.update_total()
def update_order_list(self):
self.order_listbox.delete(0, tk.END)
for item in self.order.items:
self.order_listbox.insert(tk.END, f"{item.name} - ${item.price}")
def update_total(self):
total = self.order.total_price()
self.total_label.config(text=f"Total: ${total}")
def checkout(self):
total = self.order.total_price()
if total == 0:
messagebox.showinfo("Checkout", "Your order is empty!")
else:
messagebox.showinfo("Checkout", f"Total amount to pay:
${total}\nHave a nice day!")
# Add functionality for payment processing, order confirmation,

12

etc.

def on_enter(self, widget):
self.style.configure(widget.winfo_class(), background="#007BFF")
def on_leave(self, widget):
self.style.configure(widget.winfo_class(), background="#17A2B8")
def main():
root = tk.Tk()
app = OnlineFoodOrderingApp(root)
root.mainloop()
if __name__ == "__main__":
main()
