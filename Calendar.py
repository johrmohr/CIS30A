from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Jordan's Tutoring Services")
root.geometry("350x250")

cal = Calendar(root, selectmode="day", year=2024, month=2, day=7)
cal.pack()

def grab_date():
    my_label.config(text="Today's date is " + cal.get_date())

my_button = Button(root, text="Get Date", command=grab_date)
my_button.pack()

my_label = Label(root, text="")
my_label.pack(pady=10)
root.mainloop()
