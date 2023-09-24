from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, showerror

def select_files():
    filetypes = (
        ('text files', '*.pdf'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes
        )
    lst= list(filenames)

    if lst:
        showinfo(
            title='Selected Files',
            message="The files uploaded successfully"
        )
    else:
        showerror(
            title='Error',
            message='No file selected'
        )