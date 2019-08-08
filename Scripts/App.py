import mainWindow
import fileBrowser
import tkinter as tk
from tkinter import ttk

class MainApplication:
    def __init__(self):
        self.pathWindow()
    def pathWindow(self):
        self.root = tk.Tk()
        self.root.title('LIF Classifier')
        self.file_browser = fileBrowser.Browse(self.root, initialdir=r"C:\Users",filetypes=(("All files", "*.*"),('Portable Network Graphics','*.png')),b_config="select_folder")
        self.file_browser.pack(fill='x', expand=True)
        self.root.mainloop()
        self.entered_path=self.file_browser.f_path()
        if self.entered_path=="":
            # pass
            print("NO PATH GIVEN")
        else:
            self.mainWindow(self.entered_path)
    def mainWindow(self,path):
        self.path=path
        self.root = tk.Tk()
        self.root.title('LIF Classifier-Training Files')
        self.main_window = mainWindow.mainWindow(self.root, file_loc=path)
        self.main_window.pack(fill='x', expand=True)
        self.root.mainloop()

def launchEntryApp():
    MainApplication()
     
if __name__ == '__main__': launchEntryApp()