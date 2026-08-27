from tkinter import *
from tkinter import messagebox
from storage import load_data, save_data
from PIL import Image, ImageTk

def open_cancellation_window():
    win = Toplevel()
    win.title("ابطال بیمه‌نامه")
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

    def cancel_insurance():
        data = load_data()
        number = entry_number.get()

        if number not in data:
            messagebox.showerror("خطا", "این شماره بیمه‌نامه یافت نشد")
            return

        del data[number]
        save_data(data)
        messagebox.showinfo("موفق", "بیمه‌نامه با موفقیت ابطال شد")
        win.destroy()

    Button(win, text="ابطال", bg="#87CEFA", command=cancel_insurance).pack(pady=15)