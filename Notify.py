from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

from plyer import notification
import time

t=Tk()
t.title("Desktop Notifier")
t.geometry("665x500")
img = Image.open("Notifier.jpg")
tkimg = ImageTk.PhotoImage(img)

def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_timer = timer.get()

    if get_title == "" or get_msg == "" or get_timer == "":
        messagebox.showerror("Alert", "All fields are required !")
    else:
        cur_timer =float((get_timer))*60
        messagebox.showinfo("Notifier set", "Confirm ?")
        t.destroy()
        time.sleep(cur_timer)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Desktop Notifier",
                            app_icon="Alert.ico",
                            toast=True,
                            timeout=5)

img_label = Label(t, image=tkimg).grid()

#1
title_label = Label(t, text="Title to Notify:",font=("Helvetica", 10))
title_label.place(x=30, y=230)

title = Entry(t, width="30",font=("poppins", 12))
title.place(x=170, y=230)

#2
msg_label = Label(t, text="Display Message:", font=("Helvetica", 10))
msg_label.place(x=30, y=280)

msg = Entry(t, width="40", font=("poppins", 12))
msg.place(x=170,height=60, y=280)

#3
timer_label = Label(t, text="Set Timer:", font=("Helvetica", 10))
timer_label.place(x=30, y=370)

timer = Entry(t, width="5", font=("poppins", 12))
timer.place(x=170, y=370)

#4
time_min_label = Label(t, text="min", font=("Helvetica", 10))
time_min_label.place(x=200, y=370)

#5
button = Button(t, text="SET NOTIFICATION", font=("Helvetica", 10, "bold"), fg="#FFFF00", bg="#528DFF", width=20, relief="raised", command=get_details)
button.place(x=260, y=420)

t.resizable(0,0)
t.mainloop()