import tkinter as tk
from tkinter import ttk
import fileBrowser
import mainWindow

import xgboost
import sklearn.ensemble
import sklearn.tree
import pickle
import pandas as pd
import sklearn.neighbors.typedefs
import sklearn.neighbors.quad_tree
import sklearn.tree._utils
import cython
import sklearn
import sklearn.utils._cython_blas
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
class MainApplication:
    def __init__(self):
        self.pathWindow()
    def pathWindow(self):
        self.root = tk.Tk()
        self.root.title('LIF Classifier')
        self.file_browser = fileBrowser.Browse(self.root, initialdir=r"C:\Users",filetypes=(("All files", "*.*"),('Portable Network Graphics','*.png')))
        self.file_browser.pack(fill='x', expand=True)
        self.root.mainloop()
        self.mainWindow(self.file_browser.f_path())
    def mainWindow(self,path):
        self.path=path
        self.root = tk.Tk()
        self.root.title('LIF Classifier-Data in chosen location')
        self.main_window = mainWindow.mainWindow(self.root, file_loc=path)
        self.main_window.pack(fill='x', expand=True)
        self.root.mainloop()
    def classifyWindow(self):
        pass
    def dataWindow(self):
        pass

def launchEntryApp():
    MainApplication()
def test():
    launchEntryApp()      
if __name__ == '__main__': test()