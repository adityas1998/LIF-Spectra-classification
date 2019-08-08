import classifier
import result_plot
import tkinter as tk

class classifyWindow(tk.Frame):

    def __init__(self,master,fileset=[],test_file=""):
        super().__init__(master)
        self.master=master
        self.file_index=tk.IntVar()
        self.file_index.set(0)
        self.fileset=fileset
        self._create_display_widgets(self.fileset)
        self.test_addr=test_file
        
    def _create_display_widgets(self,fileset):
        for i in fileset:
            tk.Radiobutton(self.master,text=i, variable=self.file_index, value=self.fileset.index(i)).pack(anchor='w')
        self.button=tk.Button(self.master,text="OK",command=self.quit_loop)
        self.button.pack()
       
    def quit_loop(self):
        self.master.quit()
        self.df,self.label=classifier.classify(self.fileset,self.file_index.get(),self.test_addr)
        # print("The spectra matches to:",self.label)    
        self.result_plot(self.label,self.df)
    def result_plot(self,label,df):
        self.newwin=tk.Toplevel(self.master)
        self.newwin.title("PREDICTION")   
        result_plot.resPlot(self.newwin,label,df)
        self.newwin.mainloop()
       
