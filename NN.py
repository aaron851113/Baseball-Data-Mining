import os.path
import os
import numpy as np 
from sklearn import preprocessing
import random
#from sklearn.model_selection import train_test_split
from keras.models import Sequential  
from keras.layers import Dense,Dropout  


#cross-vaildation 交叉驗證
#資料預處理
#做球員實力sorting
#把整隊的平均加進為new feature
#softmax  y_train[0,1]
#更改勝利門檻值 0.5 --> 0.8
#   + -
# +  
# -  

sum=0
train_num=10

for num in range(0,train_num):
    
    np.x_train=[]
    np.y_train=[]
    np.x_test=[]
    np.y_test=[]
    #[1,0,0,1,1]
    
    print("(第",num,"次預測)")    
    
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
    for i in range(0,40):
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
        
            np.tmp=[]        
            np.tmp.append(list(map(float,file1.readline().split(','))))
                        
            temp=[]
            for i in range(0,54):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+54]),2))
            for i in range(108,115):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+7]),2))
            for i in range(122,129):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+7]),2))
                
            np.x_train.append(temp)

            np.y_train.append(list(map(int,file1.readline().split(',')))[2]) 
            
            
            if len(np.x_train[number])!=68:
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
            np.tmp=[]        
            np.tmp.append(list(map(float,file2.readline().split(','))))
                        
            temp=[]
            for i in range(0,54):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+54]),2))
            for i in range(108,115):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+7]),2))
            for i in range(122,129):
                temp.append(round((np.tmp[0][i]-np.tmp[0][i+7]),2))
                
            np.x_test.append(temp)
            
            np.y_test.append(list(map(int,file2.readline().split(',')))[2]) 
        
    #        print(len(np.x_test[number]))
    
            if len(np.x_test[number])!=68:
                print("資料筆數錯誤")
                break
            file2.close()
            number+=1
    
    #檢查每個維度的資料數量
    #for i in range(0,len(np.x_test)):
    #    print(i,":",len(np.x_test[i]))
    
    #資料預處理
    
    
    model = Sequential()  
    model.add(Dense(units=50, input_dim=68, kernel_initializer='uniform', activation='relu'))  
    model.add(Dense(units=60, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(units=50, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(units=35, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(units=20, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))  
    print("\t[Info] Show model summary...")  
    model.summary()  
    print("")
    
    
    np.x_train = preprocessing.normalize(np.x_train, norm='l1')
    np.x_test = preprocessing.normalize(np.x_test, norm='l1')
        
    print("訓練集數量為:",len(np.x_train))
    print("測試集數量為:",len(np.x_test))
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#    train_history = model.fit(x= trainFeatures, y=trainLabels,validation_data=(testFeatures, testLabels), validation_split=0.1, epochs=50, batch_size=30, verbose=2)
    model.fit(x=np.x_train, y=np.y_train,validation_data=(np.x_test,np.y_test), validation_split=0.1, epochs=50, batch_size=20, verbose=2)
    np.y_result=[]
    np.y_result=model.predict(np.x_test)

    result=[]    
    
    for i in range(0,len(np.y_result)):
        if np.y_result[i]>=0.5:
            result.append(1)
        else :
            result.append(0)

    
    print("預測結果為： ",end='[')
    for i in range(0,len(result)):
        print(result[i],end=' ')
    print("]")
    
    print("實際結果為： ",end='[')
    for i in range(0,len(np.y_test)):
        print(np.y_test[i],end=' ')
    print("]")

       
        
    get=0
    for i in range(0,len(np.y_test)):
        if np.y_test[i]==result[i]:
            get+=1        
    print("預測準確率=",get/len(np.y_test)*100,"%")
    sum+=get/len(np.y_test)*100
    #print("預測主場勝利機率為：",np.y_test_pro)

sum/=train_num
print("NN預測",train_num,"次-預測準確總平均為：",sum,"%")


