import tkinter as tk
import dict_methods

items_in_cart = {}
item_and_amount_to_add_to_cart = []

def refresh_listbox(cart):
    listbox.delete(0, tk.END)
    for item, amount in cart.items():
        listbox.insert(tk.END, f"{item}: {amount}")


def sort_cart():
    global items_in_cart
    items_in_cart = dict_methods.sort_entries(items_in_cart)
    refresh_listbox(items_in_cart)

def add_to_cart():
    item = item_to_add.get()
    amount = int(amount_to_add.get())

    if item:
        items = [item] * amount  # iterable required by add_item()
        dict_methods.add_item(items_in_cart, items)
        refresh_listbox(items_in_cart)


# gui
root = tk.Tk()
root.title("shopping cart")

#displaying items in cart
tk.Label(root, text="items in cart").grid(row=0, column=0)

listbox = tk.Listbox(root)
listbox.grid(row=1, column=0)

tk.Button(root, text="sort items in cart", command=sort_cart).grid(row=2, column=0)

# adding item to cart
tk.Label(root, text="item to add to cart").grid(row=0, column=2)

item_to_add = tk.Entry(root)
item_to_add.grid(row=1, column=2)

tk.Label(root, text="amount of item to add").grid(row=2, column=2)


amount_to_add = tk.Spinbox(root, from_=1, to=99)
amount_to_add.grid(row=3, column=2)



tk.Button(root, text="add item to cart", command=add_to_cart).grid(row=4, column=2)

root.mainloop()