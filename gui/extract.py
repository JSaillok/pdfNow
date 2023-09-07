import tkinter
import customtkinter
from gui.gui import app

def extract_win():
    # Hide the main window
    app.withdraw()

    # Create a new window for extract functionality
    extract_window = customtkinter.CTk()
    extract_window.geometry("720x480")
    extract_window.title("Extract Elements")

    # Add your extract functionality widgets and logic here
    extract_title = customtkinter.CTkLabel(extract_window, text="Extract Elements", font=("default", 25))
    extract_title.pack(padx=15, pady=15)

    def close_extract_window():
        # Close the extract window and show the main window again
        extract_window.destroy()
        app.deiconify()

    # Add a button to close the extract window
    close_button = customtkinter.CTkButton(extract_window, text="Close", command=close_extract_window)
    close_button.pack()