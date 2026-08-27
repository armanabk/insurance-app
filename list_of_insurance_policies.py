from tkinter import *
from storage import load_data
from PIL import Image, ImageTk

def open_list_window():
    win = Toplevel()
    win.title("لیست بیمه‌نامه‌ها")
    win.geometry("1000x800")

    img = Image.open("bg.png")
    img = img.resize((1000, 800))
    bg_image = ImageTk.PhotoImage(img)
    bg_label = Label(win, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    data = load_data()

    if not data:
        Label(win, text="هیچ بیمه‌نامه‌ای ثبت نشده است", bg="#87CEFA").pack(pady=20)
        return

    for number, info in data.items():
        text = f"شماره: {number} | نوع: {info['type']} | شروع: {info['start_date']} | پایان: {info['end_date']} | مدت: {info['duration']} | مبلغ: {info['amount']}"
        Label(win, text=text, bg="#87CEFA").pack(pady=5)