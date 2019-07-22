import tkinter as tk
import classifier
class classifyWindow(tk.Frame):

    def __init__(self,master,fileset=[]):
        super().__init__(master)
        self.master=master
        self.file_index=tk.IntVar()
        self.file_index.set(0)
        self.fileset=fileset
        self._create_display_widgets(self.fileset)
        # self._display_widgets()
    def _create_display_widgets(self,fileset):
        for i in fileset:
            tk.Radiobutton(self.master,text=i, variable=self.file_index, value=self.fileset.index(i)).pack(anchor='w')
        self.button=tk.Button(self.master,text="OK",command=self.quit_loop)
        # classifier.classify(fileset,self.file_index.get())
        self.button.pack()
        # self.f_value()
    def quit_loop(self):
        # print("Selected file:",self.file_index.get())
        self.master.quit()
        classifiable=classifier.need_to_train(self.fileset,self.file_index.get())
        if classifiable==0:
            return "Need to train first, no prior training"
        else:
            return "Data Classified."
    # def f_value(self):
    #     print(self.file_index.get())

# if __name__=="__main__":
#     root=tk.Tk()
#     root.title("SELECT FILE TO CLASSIFY:")
#     classifyWindow(root,['C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-19-12-14-44-944-Petrol-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-20-14-59-42-071-Kerosene-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-20-15-14-56-361-Urea-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-20-15-54-22-256-Water-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-21-15-02-39-616-MixWaterSugar-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-21-16-16-52-948-Petrol25Diesel75-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-21-17-07-52-433-Petrol50Diesel50-Data-010.txt'])
#     root.mainloop()