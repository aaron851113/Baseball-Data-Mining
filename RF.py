import os.path
import os
import numpy as np 
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import random
#from sklearn.model_selection import train_test_split

sum=0
train_num=40
for num in range(0,train_num):
    
        
    np.x_train=[]
    np.y_train=[]
    np.x_test=[]
    np.y_test=[]
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
    
    
    np.randset=[]
    
    for i in range(0,counter):
        np.randset.append(0)
    
    group_num=counter//train_num
    
    for i in range(0,group_num):
        np.randset[i+(group_num*num)]=1
    
    print("(第",num,"筆切分群 :",i+group_num*num,")")
    
    print("共有",counter,"個資料集")
    
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
            
            np.tmp=[]        
            np.tmp.append(list(map(float,file1.readline().split(','))))
                        
            temp=[]
            for i in range(0,54):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+54]),3))
            for i in range(108,115):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+7]),3))
            for i in range(122,129):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+7]),3))
                
            np.x_train.append(temp)
        
            np.y_train.append(list(map(int,file1.readline().split(',')))[2]) 
        
    #        print(len(np.x_train[number]))
    

            file1.close()
            
            file1 = open(completeName, "r")
            np.x_train[number]+=(list(map(float,file1.readline().split(','))))
            file1.close()
            
#            print(len(np.x_train[number]))
            
            if len(np.x_train[number])!=204:
                print("資料筆數錯誤")
                break
            
            
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
            
            np.tmp=[]        
            np.tmp.append(list(map(float,file2.readline().split(','))))
                        
            temp=[]
            for i in range(0,54):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+54]),3))
            for i in range(108,115):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+7]),3))
            for i in range(122,129):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+7]),3))
                
            np.x_test.append(temp)
        
            np.y_test.append(list(map(int,file2.readline().split(',')))[2]) 
        
    #        print(len(np.x_train[number]))
                
            file2.close()
            
            file2 = open(completeName, "r")
            np.x_test[number]+=(list(map(float,file2.readline().split(','))))
            file2.close()
            
            
            if len(np.x_test[number])!=204:
                print("資料筆數錯誤")
                break
            
            number+=1
    
    #檢查每個維度的資料數量
    #for i in range(0,len(np.x_test)):
    #    print(i,":",len(np.x_test[i]))
    
    #資料預處理
    min_max_scaler = preprocessing.MinMaxScaler()
    np.x_train= min_max_scaler.fit_transform(np.x_train)
    np.x_test = min_max_scaler.fit_transform(np.x_test)
    
    np.y_result=[]
    clf = RandomForestClassifier(max_depth=15,random_state=1,n_estimators=35)
    clf.fit(np.x_train,np.y_train)
    
    r=clf.feature_importances_
    np.y_result=clf.predict(np.x_test)
    
    print("訓練集數量為:",len(np.x_train))
    print("測試集數量為:",len(np.x_test))
    

    print("預測結果為：",np.y_result)
    print("實際結果為： ",end='[')
    for i in range(0,len(np.y_test)):
        print(np.y_test[i],end=' ')
    print("]")

    get=0
    for i in range(0,len(np.y_test)):
        if np.y_test[i]==np.y_result[i]:
            get+=1        
    print("預測準確率=",get/len(np.y_test)*100,"%")
    sum+=get/len(np.y_test)*100
    #print("預測主場勝利機率為：",np.y_test_pro)
    #print(r)

sum/=train_num
print("RF預測 切分",train_num,"群 - 預測準確總平均為：",sum,"%")