from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, showerror
import os
import extractImage as ex

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
        ex.prosses_pdf(filename, ex.output_directory)
        showinfo(
            title='Selected File',
            message="The images extracted Successfully"
        )
    else:
        showerror(
            title='Error',
            message='No file selected'
        )