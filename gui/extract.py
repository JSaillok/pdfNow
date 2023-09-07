import tkinter
import customtkinter

def extract_win(app):
    # Create a new window for extract functionality
    extract_window = customtkinter.CTk()
    extract_window.geometry("720x480")
    extract_window.title("Extract Elements")
    # Hide the main window
    # gui.app.withdraw()

    # Add your extract functionality widgets and logic here
    extract_title = customtkinter.CTkLabel(extract_window, text="Extract Elements", font=("default", 25))
    extract_title.pack(padx=15, pady=15)

    def close_extract_window():
        # Close the extract window and show the main window again
        extract_window.destroy()
        app.deiconify()  # Show the main app window again

    # Add a button to close the extract window
    back_button = customtkinter.CTkButton(extract_window, text="Back", command=close_extract_window)
    back_button.pack()