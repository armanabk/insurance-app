from tkinter import *
from tkinter import messagebox
from storage import load_data, save_data
from PIL import Image, ImageTk

def open_additional_amount_window():
    win = Toplevel()
    win.title("مبلغ الحاقیه")
    win.geometry("400x300")

    img = Image.open("bg.png")
    img = img.resize((400, 300))
    bg_image = ImageTk.PhotoImage(img)
    bg_label = Label(win, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(win, text="شماره بیمه‌نامه", bg="#87CEFA").pack(pady=5)
    entry_number = Entry(win)
    entry_number.pack(pady=5)

    Label(win, text="مبلغ الحاقیه", bg="#87CEFA").pack(pady=5)
    entry_amount = Entry(win)
    entry_amount.pack(pady=5)

    def add_amount():
        data = load_data()
        number = entry_number.get()

        if number not in data:
            messagebox.showerror("خطا", "این شماره بیمه‌نامه یافت نشد")
            return

        old_amount = int(data[number]["amount"])
        new_amount = int(entry_amount.get())
        data[number]["amount"] = str(old_amount + new_amount)

        save_data(data)
        messagebox.showinfo("موفق", "مبلغ با موفقیت اضافه شد")
        win.destroy()

    Button(win, text="ثبت", bg="#87CEFA", command=add_amount).pack(pady=15)