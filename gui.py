import tkinter
import customtkinter

customtkinter.set_appearance_mode("Dark")
# customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_default_color_theme("/home/jsaillok/Documents/pdfNow/theme.json")

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
# layout = [
#     [sg.Titlebar("Welcome to pdfNow")],

#     [sg.Text("What you want to do today?")],
#     [sg.Button("Option1")],
#     [sg.Button("Option2")],
#     [sg.Button("Option3")],
#     [sg.Button("Option4")]
# ]

# window = sg.Window("pdfNow",layout, margins=(720,480))

# while True:
#     event, values= window.read()

#     if event == "Option1" or event == sg.WIN_CLOSED:
#         break

# window.close()