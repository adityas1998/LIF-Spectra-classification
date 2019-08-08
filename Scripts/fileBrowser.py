import tkinter as tk
from tkinter import filedialog as fd

class Browse(tk.Frame):
    """ Creates a frame that contains a button when clicked lets the user to select
    a file and put its filepath into an entry.
    """

    def __init__(self, master, initialdir='', filetypes=(),b_config="select_folder"):
        super().__init__(master)
        self.master=master
        self.b_config=b_config
        self.filepath = tk.StringVar()
        self._initaldir = initialdir
        self._filetypes = filetypes
        self._create_widgets()
        self._display_widgets()

    def _create_widgets(self):
        self.label = tk.Label(self, text='Data file Path:')
        self._entry = tk.Entry(self, textvariable=self.filepath)
        # get the value of string variable
        if self.b_config=="select_folder":
            self._button = tk.Button(self, text="Browse", command=self.browse)
        else:
            self._button = tk.Button(self, text="Browse", command=self.browse_file)     
        self.button2 = tk.Button(self, text = "OK",command=self.master.destroy)

    def _display_widgets(self):
        self.label.pack()
        self._entry.pack(fill='x', expand=True)
        self._button.pack()
        self.button2.pack()

    def browse(self):
        self.filepath.set(fd.askdirectory())
    def browse_file(self):
        self.filepath.set(fd.askopenfilename())
    def f_path(self):
        return self.filepath.get()

# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title('LIF Classifier')
#     file_browser = Browse(root, initialdir=r"C:\Users",filetypes=(("All files", "*.*"),('Portable Network Graphics','*.png')))
#     file_browser.pack(fill='x', expand=True)
#     root.mainloop()
    