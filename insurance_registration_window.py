from tkinter import *
from storage import load_data, save_data
from tkinter import messagebox
from PIL import Image, ImageTk

def open_registration_window():
    win = Toplevel()
    win.title("ثبت بیمه‌نامه")
    win.geometry("400x500")

    img = Image.open("bg.png")
    img = img.resize((400, 550))
    bg_image = ImageTk.PhotoImage(img)
    bg_label = Label(win, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(win, text="شماره بیمه‌نامه", bg="#87CEFA").pack(pady=5)
    entry_number = Entry(win)
    entry_number.pack(pady=5)

    Label(win, text="تاریخ شروع بیمه‌نامه", bg="#87CEFA").pack(pady=5)
    entry_start = Entry(win)
    entry_start.pack(pady=5)

    Label(win, text="تاریخ پایان بیمه‌نامه", bg="#87CEFA").pack(pady=5)
    entry_end = Entry(win)
    entry_end.pack(pady=5)

    Label(win, text="مدت بیمه‌نامه", bg="#87CEFA").pack(pady=5)
    entry_duration = Entry(win)
    entry_duration.pack(pady=5)

    Label(win, text="مبلغ بیمه‌نامه", bg="#87CEFA").pack(pady=5)
    entry_amount = Entry(win)
    entry_amount.pack(pady=5)

    Label(win, text="نوع بیمه‌نامه", bg="#87CEFA").pack(pady=5)
    insurance_type = StringVar(value="ثالث")
    Radiobutton(win, text="ثالث", variable=insurance_type, value="ثالث", bg="#87CEFA").pack()
    Radiobutton(win, text="بدنه", variable=insurance_type, value="بدنه", bg="#87CEFA").pack()

    def save_insurance():
        data = load_data()
        number = entry_number.get()

        if number in data:
            messagebox.showerror("خطا", "این شماره بیمه‌نامه قبلاً ثبت شده است")
            return

        data[number] = {
            "start_date": entry_start.get(),
            "end_date": entry_end.get(),
            "duration": entry_duration.get(),
            "amount": entry_amount.get(),
            "type": insurance_type.get()
        }

        save_data(data)
        messagebox.showinfo("موفق", "بیمه‌نامه با موفقیت ثبت شد")
        win.destroy()

    Button(win, text="ثبت", bg="#87CEFA", command=save_insurance).pack(pady=15)