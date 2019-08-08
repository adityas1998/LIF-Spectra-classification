import os
import random
import joblib
import pickle
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from matplotlib import style
import matplotlib.pyplot as plt

# This function returns the files in a given path.
def datasets(path):
    path = path
    files = []
    # r=root, d=directories, f = files
    for r, _, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))
    return files

# This function converts the given text file, of a standard type into required dataframe.
def txt_to_df(file):
  data=file.read()
  data_manipulation_step1=data.split("\n")
  data_manipulation_step2=[i.split("\t") for i in data_manipulation_step1]
  df=pd.DataFrame(data_manipulation_step2[0:len(data_manipulation_step2)-1],columns=['A','B','C','D','E','F','G','H'])
  return df

# This function is used to generate dataframes, labels which are further used to extract features and map validation results respectively.
def gen_data_frame(path):
    main_df=pd.DataFrame()
    label_dict={}
    frames=[]
    files=datasets(path)
    count=0
    for i in files:
        count+=1
        file=open(i,'r+')
        filename=i.split('.')[0]
        df=txt_to_df(file)
        df['id']=count
        frames.append(df)  
        label_dict[count]=filename
    main_df=pd.concat(frames)
    with open(os.path.join(path,"Labels.pickle"), 'wb') as handle:
      pickle.dump(label_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return (main_df,frames,label_dict)

# Column A is for Wavelength and column C is Intensity.
# This function helps in normalizing the features. Center them around their mean, divide by highest respective value.
def custom_normalizer(test_input,flag="train"):
  test_input=np.array(list(map(float,test_input)))
  test_input=test_input-test_input.mean()
  test_input=test_input/test_input.max()
  if flag=="test":
    test_input=test_input.reshape(1,-1)
  return test_input

def train(path):
    _,sub_dfs,_=gen_data_frame(path)
    train=[]
    for df_ in sub_dfs:
      feature=np.array(df_['C'])
      train.append(feature)
    labels=np.array([i for i in range(1,len(train)+1)])
    normalized_input=[]
    for train_input in train:
      normalized=custom_normalizer(train_input)
      normalized_input.append(np.array(normalized))
    
    # labels_=labels.reshape(-1,1)
    labels_=labels
    model=SVC(C=1.0,kernel='rbf',gamma='auto')
    model.fit(normalized_input,labels_)
    print("Successfully Trained!")
    joblib.dump(model,os.path.join(path,'svm2.pkl'))
   
def need_to_train(fileset):
  path=fileset[0].split("\\")[0]
  saved_model_path=os.path.join(path,"svm2.pkl")
  if os.path.exists(saved_model_path):
    return 1
  else:
    return 0  

def classify(fileset=[],file_index=0,train_addr=""):
  file_addr=fileset[file_index]
  saved_model_path=os.path.join(train_addr,"svm2.pkl")
  model=joblib.load(saved_model_path)
  file=open(file_addr,'r+')
  df=txt_to_df(file)
  #Prediction
  test_feature=custom_normalizer(df['B'],"test")
  predicted_label=model.predict(test_feature)
  with open(os.path.join(train_addr,"Labels.pickle"), 'rb') as handle:
    lab = pickle.load(handle)
  predicted_label=os.path.split(lab[predicted_label.item()])[1]
  return df,predicted_label

def plot(df,label):
  feature=np.array(df['C'])
  sub=np.array(list(map(float,feature)))
  x=np.array(list(map(float,df['A'])))
  plt.xlabel('Wavelength')
  plt.ylabel('Intensity')
  plt.title(label)  
  plt.plot(x,sub)
  plt.show()
# if __name__=="__main__":
#     x=need_to_train(['C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-19-12-14-44-944-Petrol-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-20-14-59-42-071-Kerosene-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-20-15-14-56-361-Urea-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-20-15-54-22-256-Water-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-21-15-02-39-616-MixWaterSugar-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-21-16-16-52-948-Petrol25Diesel75-Data-010.txt', 'C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-21-17-07-52-433-Petrol50Diesel50-Data-010.txt'],0)
#   # classify('C:/Users/PredatorX/Desktop/Dataset\\RefData 2017-12-19-12-14-44-944-Petrol-Data-010.txt')
#   x=datasets(r"C:/Users/PredatorX/Desktop/Dataset")
#   # x,y,z=gen_data_frame(r"C:/Users/PredatorX/Desktop/Dataset")
#   print(x)
#   # print(z)
