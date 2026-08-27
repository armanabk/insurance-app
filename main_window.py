from tkinter import *
from PIL import Image, ImageTk
from insurance_registration_window import open_registration_window
from additional_amount_window import open_additional_amount_window
from insurance_policy_cancellation_window import open_cancellation_window
from list_of_insurance_policies import open_list_window

window = Tk()
window.title("بیمه بدنه")
width = 500
height = 400


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))

window.geometry(f"{width}x{height}+{x}+{y}")
window.resizable(width=False, height=False)

img = Image.open("bg.png")
img = img.resize((width, height))
bg_image = ImageTk.PhotoImage(img)

bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

btn0 = Button(window, text="ثبت بیمه‌نامه", bg="#87CEFA", command=open_registration_window)
btn1 = Button(window, text="مبلغ الحاقیه", bg="#87CEFA", command=open_additional_amount_window)
btn2 = Button(window, text="ابطال بیمه‌نامه", bg="#87CEFA", command=open_cancellation_window)
btn3 = Button(window, text="لیست بیمه‌نامه‌ها", bg="#87CEFA", command=open_list_window)

btn0.pack(pady=10)
btn1.pack(pady=10)
btn2.pack(pady=10)
btn3.pack(pady=10)
window.mainloop()

