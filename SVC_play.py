import os.path
import os
import numpy as np 
from sklearn import svm
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest,f_regression
from sklearn.pipeline import make_pipeline

np.x_train=[]
np.y_train=[]
np.x_test=[]
np.y_test=[]
#[1,0,0,1,1]

train_path='/Users/aaron/Desktop/DataMining/ScikitLearn/train_set'

test_path='/Users/aaron/Desktop/DataMining/ScikitLearn/test_set'

#放入訓練資料集
number=0
start=0
print("放入訓練資料集")
while 1:
    
    completeName = os.path.join(train_path,str(start)+".txt")    
        
    try:
        filetry =open(completeName, "r")
        filetry.close()
    except FileNotFoundError:
#        print(str(start)+".txt","is not found.")
        break
    
    
    file1 = open(completeName, "r")
    
#    print(str(start)+".txt","is opened scuessfully.")    
    
    np.x_train.append(list(map(float,file1.readline().split(','))))
    
    np.y_train.append(list(map(int,file1.readline().split(',')))[2]) 
    
    if len(np.x_train[number])!=282:
        print("資料筆數錯誤")
        break
    
    start+=1
    number+=1
    file1.close()


#放入預測資料集
number=0
start=3000
print("放入預測資料集")
while 1:

    completeName = os.path.join(test_path,str(start)+".txt")    
    
    try:
        filetry =open(completeName, "r")
        filetry.close()
    except FileNotFoundError:
#        print(str(start)+".txt","is not found.")
        break
    
    file2 = open(completeName, "r")
    
#    print(str(start)+".txt","is loaded scuessfully.")
    
    np.x_test.append(list(map(float,file2.readline().split(','))))

    if len(np.x_test[number])!=282:
        print("資料筆數錯誤")
        break
    
    number+=1
    start+=1
    file2.close()


#檢查每個維度的資料數量
#for i in range(0,len(np.x_test)):
#    print(i,":",len(np.x_test[i]))

#資料預處理
#print(np.x_train[0])
min_max_scaler = preprocessing.MinMaxScaler()
np.x_train= min_max_scaler.fit_transform(np.x_train)
np.x_test= min_max_scaler.fit_transform(np.x_test)
#print(np.x_train[0])

clf=svm.SVC(kernel='linear')

#選取較好的80個特徵
anova_filter = SelectKBest(f_regression, k=50)
anova_svm = make_pipeline(anova_filter, clf)
anova_svm.fit(np.x_train,np.y_train)

np.y_result=anova_svm.predict(np.x_test)


print("訓練集數量為:",len(np.x_train))
print("測試集數量為:",len(np.x_test))

print("預測結果為：",np.y_result)


#print("實際結果為： ",end='[')
#for i in range(0,len(np.y_test)):
#    print(np.y_test[i],end=' ')
#print("]")

    
#get=0
#for i in range(0,len(np.y_test)):
#    if np.y_test[i]==np.y_result[i]:
#        get+=1       
#    
#print("預測準確率=",get/len(np.y_test)*100,"%")

