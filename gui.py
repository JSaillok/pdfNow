import tkinter
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("theme.json")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("pdfNow")

title = customtkinter.CTkLabel(app, text="Insert a pdf File")
title.pack(padx=10, pady=10)

def button_event():
    print("button pressed")

button = customtkinter.CTkButton(master=app,
                                 text="Let 's go!",
                                 command=button_event,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()