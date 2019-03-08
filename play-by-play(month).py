import requests
import os.path
from bs4 import BeautifulSoup 


month = input('請輸入games比賽月份...>')

for day in range(24,32):
    tmp0=int(month[0])
    tmp1=int(month[1])  
    if day<10:
        tmp2=0
        tmp3=day
    else:
        tmp2=day//10
        tmp3=day%10

    tmp=(str(tmp0)+str(tmp1)+str(tmp2)+str(tmp3))
    
    date=tmp
  
    print("日期：",date)
        
    game = 0 
    for a in range (1,4):
        for i in range (0,5):
            for j in range (0,10):
                url = "http://www.espn.com/mlb/playbyplay?gameId=38"
                    
                url = url+str(date)+str(a)            
                url = url + str(i) + str(j)
                print("game id =[",a,i,j,"]")
            
            #if requests.get(url)!=None:
                thepage = requests.get(url)
                soup = BeautifulSoup(thepage.text,'html.parser')
    #print(soup.prettify())
    #open file
                if soup.find('title').string !="MLB Baseball Scores - MLB Scoreboard - ESPN":
                    save_path = '/Users/aaron/Desktop/DataMining/games/201808'
                                
                    if game<10 :
                        name_of_file = (str(date)+"0"+str(game))
                    elif game>=10 :
                        name_of_file = (str(date)+str(game))
                    completeName = os.path.join(save_path, name_of_file+".txt")         
                    file1 = open(completeName, "w")
                    game+=1
    
    #write title to file
                    
                    print ("-",soup.title.text)
                    tofile = soup.find('title').string
                    file1.write(tofile+'\n')
    
                    page = soup.find(id="allPlaysContainer")
                    num = page.find_all('section') #每一局
                    
                    for p in num:
                        if p.find('h1')!= None :
                            #print(p.find('h1').string) #每一局的局數
                            file1.write('@ '+p.find('h1').text+'\n')    
                            num2 = p.find_all('li')
                    
                        for p2 in num2 :
                            if p2.find(class_='headline')!= None :
                            #print(p2.find(class_='headline').string)
                                file1.write('# ')
                                file1.write(p2.find(class_='headline').text+'\n')
                                num3 = p2.find_all('tr') 
                                for p3 in num3 :
                                    if p3.find('td')!= None :
                                    #print(p3.find('td').string)
                                        file1.write('- '+p3.find('td').text)
                                    if p3.find(class_='type')!= None:
                                    #print(p3.find(class_='type').string)
                                        file1.write(' $ '+p3.find(class_='type').text)
                                    if p3.find(class_='mph')!= None:
                                    #print(p3.find(class_='mph').string)
                                        file1.write(' % '+p3.find(class_='mph').text)
                                        file1.write(' \n')              
                    file1.close()        
                else:
                    continue