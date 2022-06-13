from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter
from oldpapers import OldPaper
from newpapers import NewPaper
from tkinter import ttk
import os
import threading
import webbrowser
import socket


def is_connected():
    try:
        s = socket.create_connection(("1.1.1.1", 80), 2)
        s.close()
        return True
    except Exception:
        pass
    return False


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


# customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()

selected_path = " "

no_folder_selected = "No Folder Selected"


def demo():
    webbrowser.open("https://www.youtube.com/watch?v=Fe1cZXGIvig")


def open_about_me():
    webbrowser.open("https://github.com/techjd")
    webbrowser.open("https://www.linkedin.com/in/techjd/")


def contribute():
    webbrowser.open("https://github.com/techjd/GTU-Paper-Scrapper")


menubar = Menu(window)

demo_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Demo', menu=demo_menu)
demo_menu.add_command(label='Check How To Use ? ', command=demo)

about_me = Menu(menubar, tearoff=0)
menubar.add_cascade(label='About Me', menu=about_me)
about_me.add_command(label='About Me', command=open_about_me)
about_me.add_command(label='Contribute', command=contribute)

window.config(menu=menubar)


def is_not_blank(s):
    return bool(s and not s.isspace())


def getDirectory():
    file_path = filedialog.askdirectory()
    file_name = file_path
    filePath.set(file_path)
    extra_text = ""

    if len(str(file_name)) > 20:
        extra_text = "..."
    l.config(text=filePath.get()[0:20] + extra_text)

    if is_not_blank(file_name):
        global selected_path
        selected_path = file_name
        get_paper_button.grid(row=5, pady=(50, 0), ipadx=20, ipady=10)
    else:
        get_paper_button.grid_forget()
        l.config(text=no_folder_selected)
        selected_path = no_folder_selected
    # if file_name != " ".strip():


def start():
    if not is_connected():
        messagebox.showwarning("Internet Error", "Not Connected To Internet")
    else:
        if selected_path != no_folder_selected:
            if subject_name_value.get() != subject_name_placeholder_text and subject_codes_value.get() != subject_codes_placeholder_text and is_not_blank(
                    subject_name_value.get()) and is_not_blank(subject_codes_value.get()):
                thread = threading.Thread(target=getPaper)
                thread.start()
                get_paper_button.grid_remove()
                progress_bar.grid(row=7, column=0)
                downloading_label.grid(row=6, pady=20)
                select_folder_button.state = customtkinter.DISABLED
                # select_folder_button["state"] = "disabled"

                step()
            else:
                messagebox.showwarning("Warning", "Please Fill All Fields")
        else:
            messagebox.showwarning("Warning", "Please Select a Folder")


def step():
    progress_bar.start(10)


def stop():
    progress_bar.stop()


def show_completed():
    messagebox.showinfo("Completed", "Download Completed")


def getPaper():
    print(subject_name_value.get() + " " + subject_codes_value.get())
    path = os.path.join(str(selected_path), str(subject_name_value.get()))
    os.makedirs(path, exist_ok=True)

    path_for_old_paper = os.path.join(path, 'Old Papers ( From 2017 Onwards )')
    os.makedirs(path_for_old_paper, exist_ok=True)

    path_for_new_paper = os.path.join(path, 'New Papers')
    os.makedirs(path_for_new_paper, exist_ok=True)

    StartOldPaper(path_for_old_paper, subject_codes_value.get().split(' '), subject_name_value.get()).start()
    StartNewPaper(path_for_new_paper, subject_codes_value.get().split(' '), subject_name_value.get()).start()

    stop()
    progress_bar.grid_remove()
    downloading_label.grid_remove()
    get_paper_button.grid(row=5, pady=(50, 0), ipadx=20, ipady=10)
    select_folder_button.state = customtkinter.NORMAL
    show_completed()


# Set window title
window.title('GTU Previous Year Paper Downloader')
window.iconbitmap("GTU.ico")

# Set window size
window.geometry("900x600")

window.resizable(width=0, height=0)

subjectName = customtkinter.CTkLabel(window, text="Enter Subject Name: ", text_font=('Helvetica', 18))
subjectCodes = customtkinter.CTkLabel(window, text="Enter Subject Codes: ", text_font=('Helvetica', 18))
subjectName.grid(pady=30, sticky=' ')
subjectCodes.grid(row=1, pady=30, sticky=' ')

subject_name_value = StringVar()
subject_codes_value = StringVar()

subject_name_placeholder_text = "Enter Subject Name"
subject_codes_placeholder_text = "Enter Subject Codes"

sname_entry = customtkinter.CTkEntry(window, textvariable=subject_name_value,
                                     placeholder_text=subject_name_placeholder_text,
                                     width=450,
                                     height=50,
                                     border_width=2,
                                     corner_radius=10,
                                     text_font=('Aerial', 15))
scode_entry = customtkinter.CTkEntry(window, textvariable=subject_codes_value,
                                     placeholder_text=subject_codes_placeholder_text,
                                     width=450,
                                     height=50,
                                     border_width=2,
                                     corner_radius=10,
                                     text_font=(
                                         'Aerial', 15))

sname_entry.grid(row=0, column=1)
scode_entry.grid(row=1, column=1)

hint = customtkinter.CTkLabel(window, text="Write Subject Codes By giving Space . \n For e.g. 31001 20020 29485",
                              text_font=('Helvetica', 12))
hint.grid(row=2, column=0, pady=0)

filePath = StringVar()

l = customtkinter.CTkLabel(window, text=filePath.get(), text_font=('Aerial bold', 20), width=20)
l.config(text="No Folder Selected")
l.grid(row=3, column=1, pady=(50, 0), sticky='W')

select_folder_button = customtkinter.CTkButton(text="Select Folder path \n for Papers", text_font=('Aerial bold', 20),
                                               command=getDirectory,
                                               width=120,
                                               height=32,
                                               border_width=1,
                                               corner_radius=8,
                                               text_color="white"
                                               )

select_folder_button.grid(row=3, padx=50,
                          pady=(50, 0),
                          sticky=' ', ipadx=20, ipady=10)

get_paper_button = customtkinter.CTkButton(text="Get Paper", command=start, text_font=('Aerial bold', 20),
                                           text_color="white", border_width=1)

progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, length=300, mode='indeterminate')

downloading_label = customtkinter.CTkLabel(window, text="Downloading Started", text_font=('Arial', 24))

optionmenu_var = customtkinter.StringVar(value="option 2")  # set initial value


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


combobox = customtkinter.CTkComboBox(master=window,
                                     values=["option 1", "option 2"],
                                     command=optionmenu_callback,
                                     variable=optionmenu_var)
combobox.grid(row = 10)

window.mainloop()
