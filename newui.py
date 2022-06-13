import threading
import webbrowser
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import os
import socket
from newpapers import NewPaper
from oldpapers import OldPaper


# Start here

def demo():
    webbrowser.open("https://www.youtube.com/watch?v=Fe1cZXGIvig")


def open_about_me():
    webbrowser.open("https://github.com/techjd")
    webbrowser.open("https://www.linkedin.com/in/techjd/")


def contribute():
    webbrowser.open("https://github.com/techjd/GTU-Previous-Year-Papers-Scrapper")


def show_get_paper_button():
    b0.place(
        x=561, y=652,
        width=303,
        height=87)


def show_progress_bar():
    progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, length=300, mode='indeterminate')


def show_downloading_label():
    subjectName = Label(window, bg="#FEFEFE", text="Downloading", font=('Inter', 22))


def is_connected():
    try:
        s = socket.create_connection(("1.1.1.1", 80), 2)
        s.close()
        return True
    except Exception:
        pass
    return False


# returns true if blank
def is_not_blank(s):
    return bool(s and not s.isspace())


def step():
    progress_bar.start(10)


def stop():
    progress_bar.stop()


def show_completed():
    messagebox.showinfo("Completed", "Download Completed")


class StartOldPaper:

    def __init__(self, folder_path, codes, name):
        self.folder_path = folder_path
        self.codes = codes
        self.name = name

    def start(self):
        oldpaper = OldPaper(self.folder_path, self.codes, self.name)
        oldpaper.start()


class StartNewPaper:

    def __init__(self, folder_path, codes, name):
        self.folder_path = folder_path
        self.codes = codes
        self.name = name

    def start(self):
        newpaper = NewPaper(self.folder_path, self.codes, self.name)
        newpaper.start()


def getPaper():
    selected_path = entry0.get()
    subject_name_value = entry1.get()
    subject_codes_value = entry2.get()
    # print(subject_name_value.get() + " " + subject_codes_value.get())
    path = os.path.join(str(selected_path), str(subject_name_value))
    os.makedirs(path, exist_ok=True)

    path_for_old_paper = os.path.join(path, 'Old Papers ( From 2017 Onwards )')
    os.makedirs(path_for_old_paper, exist_ok=True)

    path_for_new_paper = os.path.join(path, 'New Papers')
    os.makedirs(path_for_new_paper, exist_ok=True)

    StartOldPaper(path_for_old_paper, subject_codes_value.split(' '), subject_name_value).start()
    StartNewPaper(path_for_new_paper, subject_codes_value.split(' '), subject_name_value).start()

    stop()
    downloading.place_forget()
    progress_bar.place_forget()
    show_get_paper_button()
    show_completed()


def btn_clicked():
    if not is_connected():
        messagebox.showwarning("Can't Download", "Not Connected To Internet")
    else:
        if is_not_blank(entry1.get()) and is_not_blank(entry2.get()) and is_not_blank(entry0.get()):
            if not os.path.exists(entry0.get()):
                messagebox.showwarning("Warning", "Not Valid Path")
            else:
                # messagebox.showinfo("Info", entry1.get() + " " + entry2.get())
                thread = threading.Thread(target=getPaper)
                thread.start()
                b0.place_forget()
                progress_bar.start(10)
                progress_bar.place(x=583, y=675)
                downloading.place(x=583, y=613)


        else:
            messagebox.showerror("Error", "Please Fill All Fields")


def select_path(event):
    global output_path

    # window.withdraw()
    output_path = filedialog.askdirectory()
    entry0.delete(0, END)
    entry0.insert(0, output_path)


# End Here


window = Tk()

window.geometry("1287x767")
window.configure(bg="#fefefe")
canvas = Canvas(
    window,
    bg="#fefefe",
    height=767,
    width=1287,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    592.5, 238.5,
    image=background_img)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    770.0, 544.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#e9e4e4",
    highlightthickness=0,
    font=('Inter', 22)
)

entry0.place(
    x=585.0, y=508,
    width=370.0,
    height=71)

entry0.bind("<1>", select_path)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    781.0, 142.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#e9e4e4",
    highlightthickness=0,
    font=('Inter', 22)
)

entry1.place(
    x=585.0, y=106,
    width=392.0,
    height=71)

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = canvas.create_image(
    880.5, 311.5,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#e9e4e4",
    highlightthickness=0,
    font=('Inter', 22))

entry2.place(
    x=585.0, y=275,
    width=591.0,
    height=71)


img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=561, y=652,
    width=303,
    height=87)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=open_about_me,
    relief="flat")

b1.place(
    x=74, y=331,
    width=327,
    height=107)

img2 = PhotoImage(file=f"img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=contribute,
    relief="flat")

b2.place(
    x=72, y=438,
    width=327,
    height=107)

img3 = PhotoImage(file=f"img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=demo,
    relief="flat")

b3.place(
    x=72, y=545,
    width=327,
    height=107)

# downloading = canvas.create_text(
#     684.5, 624.5,
#     text="Downloading",
#     fill="#000000",
#     font=("Inter", int(28.0)))
#
#
# canvas.delete(downloading)

progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, length=300, mode='indeterminate')
downloading = Label(window, bg="#FEFEFE", text="Downloading", font=('Inter', 28))

window.resizable(False, False)
window.mainloop()
