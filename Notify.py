from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

from plyer import notification
import time
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

