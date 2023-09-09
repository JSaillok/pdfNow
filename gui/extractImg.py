import sys
import os
path = os.path.abspath("backend")
sys.path.append(path)
import customtkinter
from files import select_file

def images_win(extract_window):
    images_window = customtkinter.CTk()
    images_window.geometry("720x480")
    images_window.title("pdfNow")

    images_title = customtkinter.CTkLabel(images_window, text="Select the pdf to fetch the Images", font=("default", 25))
    images_title.pack(padx=15, pady=15)

    button_frame = customtkinter.CTkFrame(images_window)
    button_frame.pack(pady=20)

    # open button
    open_button = customtkinter.CTkButton(master=button_frame,
                                    text='Open a File',
                                    command=select_file,
                                    width=120,
                                    height=80,
                                    border_width=0,
                                    corner_radius=8,
                                    font= ("default",20))  
    open_button.pack(expand=True)