import tkinter as tk

root = tk.Tk()
root.title("shopping cart")

#displaying items in cart
tk.Label(root, text="items in cart").grid(row=0, column=0)

# adding item to cart
tk.Label(root, text="item to add to cart").grid(row=0, column=2)
tk.Entry(root).grid(row=1, column=2)
tk.Label(root, text="amount of item to add").grid(row=2, column=2)
tk.Entry(root).grid(row=3, column=2)
tk.Button(root, text="add item to cart").grid(row=4, column=2)

root.mainloop()