import classifier
import tkinter as tk

class resPlot(tk.Frame):
    """ Creates a frame that contains a button when clicked lets the user to select
    a file and put its filepath into an entry.
    """
    def __init__(self, master,label,df):
        super().__init__(master)
        self.master=master
        self.label=label
        self.df=df
        self.tkstrvar = tk.StringVar()
        self.tkstrvar.set(self.label)
        self._create_display_widgets()
     
    def _create_display_widgets(self):
        self.msg = tk.Label(self.master, text = "Closest match: "+self.tkstrvar.get())
        self.msg.pack()
        self.button=tk.Button(self.master,text="Plot Spectrum",command=lambda:classifier.plot(self.df,self.label))
        self.button.pack()
