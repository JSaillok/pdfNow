import tkinter
import customtkinter
from extract import extract_win

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("gui/theme.json")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("pdfNow")

title = customtkinter.CTkLabel(app, text="WELCOME STRANGER", font=("default", 25))
title.pack(padx=15, pady=15)

# Create a frame to contain the buttons
button_frame = customtkinter.CTkFrame(app)
button_frame.pack(pady=20)

def button_event():
    print("button pressed")

# Create four buttons
button1 = customtkinter.CTkButton(master=button_frame,
                                  text="Extract Elements",
                                  command=extract_win,
                                  width=120,
                                  height=80,
                                  border_width=0,
                                  corner_radius=8,
                                  font= ("default",20))
button2 = customtkinter.CTkButton(master=button_frame,
                                  text="Merge",
                                  command=button_event,
                                  width=120,
                                  height=80,
                                  border_width=0,
                                  corner_radius=8,
                                  font= ("default",20))
button3 = customtkinter.CTkButton(master=button_frame,
                                  text="Split",
                                  command=button_event,
                                  width=120,
                                  height=80,
                                  border_width=0,
                                  corner_radius=8,
                                  font= ("default",20))

# Arrange the buttons in a 2x2 grid
button1.grid(row=0, column=0, padx=40, pady=20)
button2.grid(row=1, column=0, padx=40, pady=20)
button3.grid(row=2, column=0, padx=40, pady=20)

if __name__ == "__main__":
    app.mainloop()