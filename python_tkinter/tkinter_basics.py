from tkinter import *
from PIL import Image, ImageTk

first_root= Tk()
first_root.title("First GUI")
first_root.geometry("400x400")
first_root.config(bg="lightblue")
# first_root.maxsize(500, 500)
# first_root.minsize(200, 200)
img = Image.open("8am_charlotee.jpg")
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)
label1 = Label(first_root, text="Welcome to Python GUI", font="Arial 20 bold", fg="red", bg="lightblue")
label2= Label(first_root, image=img)
text_label=Label(text="This is a text label", font="Arial 25 bold", fg="blue", bg="lightblue", relief=RAISED, bd=5)
text_label.pack(anchor=NW,fill=X,padx=20,pady=10)
label1.pack()
label2.pack(anchor=NE, padx=20, pady=20)
first_root.mainloop()
