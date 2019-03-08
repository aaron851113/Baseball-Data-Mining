import requests
import os.path
from bs4 import BeautifulSoup 

teams={'BAL','TOR','BOS','NYY','TBR','NYM','ATL','PHI','WSN','MIA',
       'MIN','CLE','CHW','DET','KCR','PIT','MIL','CHC','STL','CIN',
       'LAA','HOU','SEA','OAK','TEX','ARI','SFG','COL','LAD','SDP'}

day = input('請輸入打擊投球截止日...>')

name_of_file=str(day)
save_path1 = '/Users/aaron/Desktop/DataMining/batting'
completeName = os.path.join(save_path1, name_of_file+".txt")         
file1 = open(completeName, "w")

save_path2 = '/Users/aaron/Desktop/DataMining/pitching'
completeName = os.path.join(save_path2, name_of_file+".txt")         
file2 = open(completeName, "w")

number=1

for i in teams :
    url='https://www.baseball-reference.com/teams/'
    
    url=url+i
    
    url=url+'/2018.shtml'
    print("NOW Teams= [",i,"]")
    thepage = requests.get(url)
    soup = BeautifulSoup(thepage.text,'html.parser')
    """
    head=soup.find('head')
    name_of_file=head.find('title').string
    print(head.find('title').string)
    """
    
    
    #file1.write(head.find('title').text+'\n')
    
    
    first = soup.find(id="all_team_batting")
    tbody = first.find('tbody')
    num = tbody.find_all('tr')

    
    for p in num:
        count=0
        if p.find(attrs={"data-stat": "AB"}).string!="AB":
           if p.find(attrs={"data-stat": "PA"}).string!="0":
               if p.find('a')!= None :
                   print(p.find('a').string, end=" ")
                   file1.write('# '+p.find('a').text+' ')
                   file1.write('~ '+i+' ')
                   count+=1
               if p.find(attrs={"data-stat": "G"})!= None :
                   print(p.find(attrs={"data-stat": "G"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"G"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "PA"})!= None :
                   print(p.find(attrs={"data-stat": "PA"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"PA"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "AB"})!= None :
                   print(p.find(attrs={"data-stat": "AB"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"AB"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "R"})!= None :
                   print(p.find(attrs={"data-stat": "R"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"R"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "H"})!= None :
                   print(p.find(attrs={"data-stat": "H"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"H"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "2B"})!= None :
                   print(p.find(attrs={"data-stat": "2B"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"2B"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "3B"})!= None :
                   print(p.find(attrs={"data-stat": "3B"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"3B"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "HR"})!= None :
                   print(p.find(attrs={"data-stat": "HR"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"HR"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "RBI"})!= None :
                   print(p.find(attrs={"data-stat": "RBI"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"RBI"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "BB"})!= None :
                   print(p.find(attrs={"data-stat": "BB"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"BB"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "SO"})!= None :
                   print(p.find(attrs={"data-stat": "SO"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"SO"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "batting_avg"}).string!= None :
                   print(p.find(attrs={"data-stat": "batting_avg"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"batting_avg"}).text+' ')
                   count+=1
               else:
                   print('.000',end=" ")
                   file1.write('~ '+'.000'+' ')
                   count+=1
               if p.find(attrs={"data-stat": "onbase_perc"}).string!= None :
                   print(p.find(attrs={"data-stat": "onbase_perc"}).string,end=" ")
                   file1.write('~ '+p.find(attrs={"data-stat":"onbase_perc"}).text+' ')
                   count+=1
               else:
                   print('.000',end=" ")
                   file1.write('~ '+'.000'+' ')
                   count+=1
               if p.find(attrs={"data-stat": "slugging_perc"}).string!= None :
                   print(p.find(attrs={"data-stat": "slugging_perc"}).string)
                   file1.write('~ '+p.find(attrs={"data-stat":"slugging_perc"}).text+' ')
                   count+=1
               else:
                   print('.000')
                   file1.write('~ '+'.000'+' ')
                   count+=1
               if count!=15:
                   print('error!!!')
                   break
               file1.write('\n')
     
    first = soup.find(id="all_team_pitching")
    tbody = first.find('tbody')
    num = tbody.find_all('tr')

    for p in num:
        count=0
        if p.find(attrs={"data-stat":"G"}).string!='G':
           if p.find(attrs={"data-stat": "G"}).string!='0':
               if p.find('a')!= None :
                   print(p.find('a').string, end=" ")
                   file2.write('# '+p.find('a').text+' ')
                   file2.write('~ '+i+' ')
                   count+=1
               if p.find(attrs={"data-stat": "W"})!= None :
                   print(p.find(attrs={"data-stat": "W"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"W"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "L"})!= None :
                   print(p.find(attrs={"data-stat": "L"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"L"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "earned_run_avg"})!= None :
                   print(p.find(attrs={"data-stat": "earned_run_avg"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"earned_run_avg"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat": "win_loss_perc"}).string!=None:
                   print(p.find(attrs={"data-stat": "win_loss_perc"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"win_loss_perc"}).text+' ')
                   count+=1
               else:
                   print('.000',end=" ")
                   file2.write('~ '+'.000'+' ')
                   count+=1
               if p.find(attrs={"data-stat":"G"})!= None :
                   print(p.find(attrs={"data-stat": "G"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"G"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat":"GS"})!= None :
                   print(p.find(attrs={"data-stat": "GS"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"GS"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat":"GF"})!= None :
                   print(p.find(attrs={"data-stat": "GF"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"GF"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat":"SV"})!= None :
                   print(p.find(attrs={"data-stat": "SV"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"SV"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat":"IP"})!= None :
                   print(p.find(attrs={"data-stat": "IP"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"IP"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat":"H"})!= None :
                   print(p.find(attrs={"data-stat": "H"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"H"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat":"R"})!= None :
                   print(p.find(attrs={"data-stat": "R"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"R"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat":"ER"})!= None :
                   print(p.find(attrs={"data-stat": "ER"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"ER"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat":"HR"})!= None :
                   print(p.find(attrs={"data-stat": "HR"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"HR"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat":"BB"})!= None :
                   print(p.find(attrs={"data-stat": "BB"}).string,end=" ")
                   file2.write('~ '+p.find(attrs={"data-stat":"BB"}).text+' ')
                   count+=1
               if p.find(attrs={"data-stat":"SO"})!= None :
                   print(p.find(attrs={"data-stat": "SO"}).string)
                   file2.write('~ '+p.find(attrs={"data-stat":"SO"}).text+' ')
                   count+=1
               if count!=16:
                   print('error!!!')
                   break
               
               file2.write('\n')

    print('--- NO.',number,'----[',i,']---Finish---')
    number+=1
file1.close()
file2.close()



