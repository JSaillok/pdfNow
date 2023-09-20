import sys
import os
path = os.path.abspath("backend")
sys.path.append(path)
import customtkinter
from files import select_file1

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
                                    command=select_file1,
                                    width=120,
                                    height=80,
                                    border_width=0,
                                    corner_radius=8,
                                    font= ("default",20))  
    open_button.pack(expand=True)

    

    def close_img_window():
        # Close the extract window and show the main window again
        images_window.destroy()
        extract_window.deiconify()  # Show the main app window again

    # Add a button to close the extract window
    back_button = customtkinter.CTkButton(images_window, text="Back", command=close_img_window)
    back_button.pack()