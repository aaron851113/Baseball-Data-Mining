import requests
import os.path
from bs4 import BeautifulSoup 
import numpy as np 

day = input('請輸入先發名單比賽日期...>')
url = 'https://sports.yahoo.com/mlb/scoreboard/?confId=&schedState=2&dateRange=2018'

tmp0=int(day[0])
tmp1=int(day[1])
tmp2=int(day[2])
tmp3=int(day[3])+1
if tmp3==10:
    tmp2+=1
    tmp3=0

url=url+'-'+str(tmp0)+str(tmp1)+'-'+str(tmp2)+str(tmp3)

#print(url)
thepage = requests.get(url)
soup = BeautifulSoup(thepage.text,'html.parser')

scoreboard = soup.find(id="scoreboard-group-2")

mb30 = scoreboard.find_all(class_="Mb(30px)")

number = 0
np.url=[]

for div in mb30:
    if div.find('h3').text!='Finished':
        continue
    ul = div.find("ul")
    for l in div.find_all("li") :
        for a in l.find_all("a") :
#            print(a.get('href'))
            tmp_url=str(a.get('href'))
            tmp_url="https://sports.yahoo.com"+tmp_url
            if tmp_url.find('video')!=-1:
                continue
            if len(tmp_url)>50:
                np.url.append(tmp_url)
                print(number,":",np.url[number])
                number+=1



game=0

for i in np.url :
    
    if game<10: 
        name_of_file = day+"0"+str(game)
    else:
        name_of＿file = day+str(game)
    
    
    
    thepage = requests.get(i)
    soup = BeautifulSoup(thepage.text,'html.parser')
    
    if soup.find(class_="player-stats") ==None:
        continue
    
    save_path = '/Users/aaron/Desktop/DataMining/先發名單'

    completeName = os.path.join(save_path,name_of_file+".txt")         
    
    file1 = open(completeName,"w")
     
    save_path = '/Users/aaron/Desktop/DataMining/先發名單'

    first = soup.find(class_="player-stats")
    second = first.find_all('tbody')
    
    num=1
    count=0
    b1=[]
    b2=[]
    
    for body in second:
        if num==1 :
            third = body.find_all('tr')
            for tr in third:
                if tr.find('a')!=None:
                    if tr.find(class_="D(ib) Pstart(25px)")==None:
                        file1.write(tr.find('a').text+'\n')
                        count+=1
                        b1.append(tr.find('a').string)
        elif num==2:
            third = body.find_all('tr')
            for tr in third:
                if tr.find('a')!=None:
                    if tr.find(class_="D(ib) Pstart(25px)")==None:
                        file1.write(tr.find('a').text+'\n')
                        count+=1
                        b2.append(tr.find('a').string)
        elif num==3 or num==4:
            third = body.find('tr')
            for tr in third:
                if tr.find('a')!=None:
                    file1.write(tr.find('a').text+'\n')
                    count+=1
        num+=1
    
    file1.write(soup.find('title').text)
    
    
    file1.close()
    print(game,":","person:",count)
    game+=1


