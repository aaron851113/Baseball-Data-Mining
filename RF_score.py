import os.path
import os
import numpy as np 
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import random
#from sklearn.model_selection import train_test_split


train_num=1000
merror=0
for num in range(0,train_num):
    
    print("(第",num,"次預測)")
    
    np.x_train=[]
    np.y_train=[]
    np.x_test=[]
    np.y_test=[]
    np.y1=[]
    np.y2=[]
    #[1,0,0,1,1]
    
    
    train_path='/Users/aaron/Desktop/DataMining/ScikitLearn/train_set'
    
    
    counter=0
    start=0
    
    while 1:
        completeName = os.path.join(train_path,str(start)+".txt")    
        try:
            filetry =open(completeName, "r")
            filetry.close()
            counter+=1
            start+=1
        except FileNotFoundError:
            break
        
    print("共有",counter,"個資料集")
    
    np.randset=[]
    
    for i in range(0,counter):
        np.randset.append(0)
    
    random.seed()
    for i in range(0,20):
        ran=random.randint(1,counter-1)
        while np.randset[ran]==1:
            ran=random.randint(1,counter-1)
        np.randset[ran]=1
    
    #放入訓練資料集
    start=-1
    number=0
    print("放入訓練資料集")
    
    while 1:
        start+=1
        if start>=counter:
            break
        
        if np.randset[start]==0:
            completeName = os.path.join(train_path,str(start)+".txt")    
            
            try:
                filetry =open(completeName, "r")
                filetry.close()
            except FileNotFoundError:
                continue
                
            file1 = open(completeName, "r")
            
    #        print(str(start)+".txt","is opened scuessfully.")    
        
            np.x_train.append(list(map(float,file1.readline().split(','))))
        
            np.y1.append(list(map(int,file1.readline().split(','))))
            
            np.y_train.append(np.y1[number][0]+np.y1[number][1])
        
    #        print(len(np.x_train[number]))
    
            if len(np.x_train[number])!=136:
                print("資料筆數錯誤")
                break
            file1.close()
            number+=1
        
    
    
    #放入預測資料集
    start=-1
    number=0
    print("放入預測資料集")
    
    while 1:
        start+=1
        if start>=counter:
            break
        if np.randset[start]==1:
            
            completeName = os.path.join(train_path,str(start)+".txt")    
            try:
                filetry =open(completeName, "r")
                filetry.close()
            except FileNotFoundError:
                continue
                
            file2 = open(completeName, "r")
            
    #        print(str(start)+".txt","is opened scuessfully.")    
        
            np.x_test.append(list(map(float,file2.readline().split(','))))
        
            np.y2.append(list(map(int,file2.readline().split(','))))
            
            np.y_test.append(np.y2[number][0]+np.y2[number][1])
            
        
    #        print(len(np.x_train[number]))
    
            if len(np.x_train[number])!=136:
                print("資料筆數錯誤")
                break
            file2.close()
            number+=1
    
    
    #檢查每個維度的資料數量
    #for i in range(0,len(np.x_test)):
    #    print(i,":",len(np.x_test[i]))
    
    #資料預處理

    min_max_scaler = preprocessing.MinMaxScaler()
    np.x_train= min_max_scaler.fit_transform(np.x_train)
    np.x_test = min_max_scaler.fit_transform(np.x_test)
    
    np.y_result=[]
    clf = RandomForestClassifier(max_depth=5,random_state=0,n_estimators=14)
    clf.fit(np.x_train,np.y_train)
    
    r=clf.feature_importances_
    np.y_result=clf.predict(np.x_test)
    
    print("訓練集數量為:",len(np.x_train))
    print("測試集數量為:",len(np.x_test))
    
    print("預測結果為：",np.y_result)
    print("實際結果為： ",end='[')
    
    for i in range(0,len(np.y_test)):
        print(np.y_test[i],end='  ')
    print("]")
    
    
    sum=0
    for i in range(0,len(np.y_test)):
        sum+=abs(np.y_test[i]-np.y_result[i])
    
    merror+=(sum/len(np.y_test))
    

merror/=train_num
print("RF預測",train_num,"次-預測準確誤差值為：",merror)
