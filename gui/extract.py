import customtkinter
import extractImg
import extractTb

def extract_win(app):
    # Create a new window for extract functionality
    extract_window = customtkinter.CTk()
    extract_window.geometry("720x480")
    extract_window.title("pdfNow")

    # Add your extract functionality widgets and logic here
    extract_title = customtkinter.CTkLabel(extract_window, text="Extract Elements", font=("default", 25))
    extract_title.pack(padx=15, pady=15)

    # Create a frame to contain the buttons
    button_frame = customtkinter.CTkFrame(extract_window)
    button_frame.pack(pady=20)
    
    def call_images():
        # Hide the main window
        extract_window.withdraw()
        extractImg.images_win(extract_window)  # Pass the app instance to the extract window
    
    def call_tables():
        # Hide the main window
        extract_window.withdraw()
        extractTb.tables_win(extract_window)  # Pass the app instance to the extract window
    
    # Create buttlinksons
    button1 = customtkinter.CTkButton(master=button_frame,
                                  text="Extract Images",
                                  command=call_images,
                                  width=120,
                                  height=80,
                                  border_width=0,
                                  corner_radius=8,
                                  font= ("default",20))
    button2 = customtkinter.CTkButton(master=button_frame,
                                  text="Extract Tables",
                                  command=call_tables,
                                  width=120,
                                  height=80,
                                  border_width=0,
                                  corner_radius=8,
                                  font= ("default",20))

    # Arrange the buttons in a 2x2 grid
    button1.grid(row=0, column=0, padx=40, pady=20)
    button2.grid(row=1, column=0, padx=40, pady=20)

    def close_extract_window():
        # Close the extract window and show the main window again
        extract_window.destroy()
        app.deiconify()  # Show the main app window again

    # Add a button to close the extract window
    back_button = customtkinter.CTkButton(extract_window, text="Back", command=close_extract_window)
    back_button.pack()