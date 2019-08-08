import os
import classifier
import fileBrowser
import tkinter as tk
import classifywindow
from tkinter import ttk
from tkinter import filedialog as fd

class mainWindow(tk.Frame):

    def __init__(self, master, file_loc=''):
        super().__init__(master)
        self.master=master
        self.filepath = file_loc
        self._create_widgets()
        self._display_widgets()
    
    def  classify_window(self,dataFiles):
        self.test_files=tk.StringVar()
        self.test_files.set(fd.askdirectory())
        if self.test_files.get()=="":
            print("Enter the directory location for testing files.")
        else:
            self.file_set=self.fileList(self.test_files.get())
            self.list_from_tuple=[i[1] for i in self.file_set]
            self.newwin=tk.Toplevel(self.master)
            self.newwin.title("SELECT FILE TO CLASSIFY:")
            classifywindow.classifyWindow(self.newwin,self.list_from_tuple,self.filepath)
        
    def _create_widgets(self):
        self.button1 = tk.Button(self, text = "Train",width=15,command=lambda:classifier.train(self.filepath))
        self.button2 = tk.Button(self, text = "Classify",width=15,command=lambda: self.classify_check())
        self.scrollbar = tk.Scrollbar(self.master) 
        self.listBox = tk.Listbox(self.master, width=60, yscrollcommand = self.scrollbar.set ) 
        self.scrollbar.config( command = self.listBox.yview ) 
        self.listPopulator(self.listBox,self.filepath)
        
    def _display_widgets(self):
        self.button1.pack()
        self.button2.pack()
        self.scrollbar.pack( side = tk.LEFT, fill = 'y' ) 
        self.listBox.pack( side = tk.LEFT, fill = tk.BOTH ) 

    def fileList(self,filepath):
        self.dataFiles=[]
        for file in os.listdir(filepath):
            self.fType=file.split('.')[1]
            if self.fType=="txt":
                self.dataFiles.append((file,os.path.join(filepath,file)))
        return self.dataFiles

    def listPopulator(self,listBox,filepath):
        self.fList=self.fileList(filepath)
        for file in range(len(self.fList)):
            self.listBox.insert(tk.END, self.fList[file][0]) 

    def classify_check(self):
        self.dataFiles=self.fileList(self.filepath)
        self.list_from_tuple=[i[1] for i in self.dataFiles]
        if classifier.need_to_train(self.list_from_tuple):
            self.classify_window(self.dataFiles)
        else:
            print("Need to train first, no prior training")


# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title('LIF Classifier')
#     main_window = mainWindow(root, file_loc=r"C:/Users/PredatorX/Desktop/Dataset")
#     main_window.pack(fill='x', expand=True)
#     root.mainloop()
