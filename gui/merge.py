import customtkinter
import sys
import os
path = os.path.abspath("backend")
sys.path.append(path)
from multFiles import select_files

def merge_win(app):
    merge_window = customtkinter.CTk()
    merge_window.geometry("720x480")
    merge_window.title("pdfNow")

    merge_title = customtkinter.CTkLabel(merge_window, text="Select the pdfs to merge them", font=("default", 25))
    merge_title.pack(padx=15, pady=15)

    button_frame = customtkinter.CTkFrame(merge_window)
    button_frame.pack(pady=20)

    # open button
    open_button = customtkinter.CTkButton(master=button_frame,
                                    text='Open a File',
                                    command=select_files,
                                    width=120,
                                    height=80,
                                    border_width=0,
                                    corner_radius=8,
                                    font= ("default",20))  
    open_button.pack(expand=True)

    def close_merge_window():
        # Close the extract window and show the main window again
        merge_window.destroy()
        app.deiconify()  # Show the main app window again

    # Add a button to close the extract window
    back_button = customtkinter.CTkButton(merge_window, text="Back", command=close_merge_window)
    back_button.pack()