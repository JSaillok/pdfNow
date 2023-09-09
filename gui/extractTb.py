import sys
import os
path = os.path.abspath("backend")
sys.path.append(path)
import customtkinter
from files import select_file

def tables_win(extract_window):
    tables_window = customtkinter.CTk()
    tables_window.geometry("720x480")
    tables_window.title("pdfNow")

    tables_title = customtkinter.CTkLabel(tables_window, text="Select the pdf to fetch the Tables", font=("default", 25))
    tables_title.pack(padx=15, pady=15)

    button_frame = customtkinter.CTkFrame(tables_window)
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

    def close_tb_window():
        # Close the extract window and show the main window again
        tables_window.destroy()
        extract_window.deiconify()  # Show the main app window again

    # Add a button to close the extract window
    back_button = customtkinter.CTkButton(tables_window, text="Back", command=close_tb_window)
    back_button.pack()