import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
img = tk.PhotoImage(file='.\in_class_project\images\player.png')
canvas.create_image(250, 250, image=img)
root.mainloop()