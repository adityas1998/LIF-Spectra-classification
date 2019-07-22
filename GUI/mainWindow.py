import tkinter as tk
import classifywindow
from tkinter import ttk
import classifier
import os

class mainWindow(tk.Frame):

    def __init__(self, master, file_loc=''):
        super().__init__(master)
        self.master=master
        self.filepath = file_loc
        self.dataFiles=[]
        self._create_widgets()
        self._display_widgets()
    def  classify_window(self,dataFiles):
        self.newwin=tk.Toplevel(self.master)
        self.newwin.title("SELECT FILE TO CLASSIFY:")
        self.list_from_tuple=[i[2] for i in self.dataFiles]
        classifywindow.classifyWindow(self.newwin,self.list_from_tuple)
        # print(self.list_from_tuple)
        # classify_window.pack(fill='x',expand=True)

    def _create_widgets(self):
        self.button1 = tk.Button(self, text = "Train",width=25,command=lambda:classifier.train(self.filepath))
        self.button2 = tk.Button(self, text = "Classify",width=25,command=lambda: self.classify_window(self.dataFiles))
        self.scrollbar = tk.Scrollbar(self.master) 
        self.listBox = tk.Listbox(self.master, width=60, yscrollcommand = self.scrollbar.set ) 
        self.scrollbar.config( command = self.listBox.yview ) 
        self.listPopulator(self.listBox,self.filepath)
        # self.button1 = tk.Button(self, text="Train",width=25, command=self.master.destroy)
        # self.button2 = tk.Button(self, text="Classify",width=25, command=self.master.destroy)
    
        
    def _display_widgets(self):
        self.button1.pack()
        self.button2.pack()
        self.scrollbar.pack( side = tk.LEFT, fill = 'y' ) 
        self.listBox.pack( side = tk.LEFT, fill = tk.BOTH ) 

    def fileList(self,filepath):
        for file in os.listdir(filepath):
            self.fType=file.split('.')[1]
            if self.fType=="txt":
                self.fName=file.split('-')[7]
                self.dataFiles.append((file,self.fName,os.path.join(filepath,file)))
        return self.dataFiles


    def listPopulator(self,listBox,filepath):
        self.fList=self.fileList(filepath)
        for file in range(len(self.fList)):
            self.listBox.insert(tk.END, self.fList[file][0]) 


# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title('LIF Classifier')
#     main_window = mainWindow(root, file_loc=r"C:/Users/PredatorX/Desktop/Dataset")
#     main_window.pack(fill='x', expand=True)
#     root.mainloop()
