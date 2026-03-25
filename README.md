# MechaMunchGUI
MVP that manages basic shopping cart activities through a graphical interface.

Personally I chose the tkinter package because it is built into Python and requires no installation, making it perfect for a MVP. This reduced the setup time and avoided possible compatibility issues. tkinter also provided all the basic widgets I needed such as buttons, labels, entry fields, and listboxes to display and manage the shopping cart. Its straightforward syntax made it easy to connect the GUI to my existing backend functions like add_item() and sort_entries().

I considered other frameworks such as PyQt and Kivy. While PyQt offers a more modern and appealing interface, its more complex and has a steeper learning curve, which would likely increase my development time. Kivy seems powerful and supports touch interfaces, but it is less suited for simple desktop applications, requires additional setup and i didn't need touch interfaces. For the MVP these options were unnecessary because they provide more features than required while being more time consuming to learn.

tkinter fits well with the MVP philosophy because it allows for rapid development of a functional interface without overcomplicating anything. Since the goal was to demonstrate the core functionality e.g. displaying cart contents, adding items, and sorting entries rather than focusing on design or advanced user experience. Using tkinter helped me keep the code simple, readable, and maintainable.

A limitation I encountered was the lack of more modern styling options in tkinter, which made the interface look "basic" compared to how it may with other frameworks. However since i only needed an MVP, I focused on creating a clear and organised layout using the grid system, trying to ensure the interface remains user friendly despite its simplicity.
