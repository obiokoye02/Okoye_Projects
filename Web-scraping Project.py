#setup imports
import requests as r
from bs4 import BeautifulSoup
import csv
import time as t
import random as rnd

#set scrape settings variables, edit as necessasry for your environment.
urltoget='http://drd.ba.ttu.edu/isqs3358/hw/hw1/'
fp= '/Users/Travi/Downloads/' 
filename1 = 'dataout.csv'
lowval = 5
highval = 7

#request page
res=r.get(urltoget)
 
#convert response into soup 
soup = BeautifulSoup(res.content, 'lxml')

#subdivide page, by finding this div first.  Notice the extra val down in the footer we want to exclude.
usrs=soup.find('div', attrs={'id':'UsrIndex'})

usrlist = usrs.find_all('tr')

with open(fp + filename1,'w') as dataout:
    datawriter = csv.writer(dataout, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    #write header row
    datawriter.writerow(['Rank', 'user_id', 'fname', 'lname', 'avg_water', 'avg_sleep', 'avg_step', 'day', 'day_water_amt', 'day_sleep_amt', 'day_step_amt', 'metric'])
    for usr in usrlist:
        usrtds = usr.find_all('td')
        if len(usrtds) == 7:
            href = usrtds[0].find('a')['href']
            usrres = r.get(urltoget + href)
            usrsoup = BeautifulSoup(usrres.content, 'lxml')
            usrdetail = usrsoup.find('div', attrs={'id' : 'UsrDetail'}).find_all('tr')
            for daily in usrdetail:
                tds = daily.find_all('td')
                if (len(tds) == 4):
                    
                    datawriter.writerow([
                        usrtds[1].text,
                        href.split('=')[1],
                        usrtds[2].text.split(' ')[0],
                        usrtds[2].text.split(' ')[1],
                        usrtds[4].text,
                        usrtds[3].text,
                        usrtds[5].text,
                        tds[0].text,
                        tds[2].text,
                        tds[1].text,
                        tds[3].text,
                        usrtds[6].text
                    ])
                
                    #left in commented print statements for you to use as debug
                    #if you didn't want to output the file.  Just comment
                    #lines 41-54 and uncomment 59-70                    
                    #print('rank', usrtds[1].text)
                    #print('user_id', href.split('=')[1])
                    #print('fname', usrtds[2].text.split(' ')[0])
                    #print('lname', usrtds[2].text.split(' ')[1])
                    #print('avg_water', usrtds[4].text)
                    #print('avg_sleep', usrtds[3].text)
                    #print('avg_step', usrtds[5].text)
                    #print('day', tds[0].text)
                    #print('water', tds[2].text)
                    #print('sleep', tds[1].text)
                    #print('step', tds[3].text)
                    #print('metric', usrtds[6].text)
                    

                            
    timetosleep = rnd.randint(lowval, highval) + rnd.random()
    t.sleep(timetosleep)
                            