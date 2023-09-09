from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, showerror

def select_file():
    filetypes = (
        ('text files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if filename:
        showinfo(
            title='Selected File',
            message=filename
        )
    else:
        showerror(
            title='Error',
            message='No file selected'
        )