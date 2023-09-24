from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, showerror
import extractImage as ei
import extractTable as et

def select_file1():
    filetypes = (
        ('text files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if filename:
        # Extract Images
        ei.process_pdf(filename, ei.output_directory)
        showinfo(
            title='Selected File',
            message="The images extracted Successfully/nCheck folder pdfNow/Images"
        )
    else:
        showerror(
            title='Error',
            message='No file selected'
        )

def select_file2():
    filetypes = (
        ('text files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if filename:
        # Extract Tables
        et.tables_pdf(filename, et.output_directory)
        showinfo(
            title='Selected File',
            message="The tables extracted Successfully/nCheck folder pdfNow/Tables"
        )
    else:
        showerror(
            title='Error',
            message='No file selected'
        )