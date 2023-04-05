import requests
from bs4 import BeautifulSoup
import os

url='https://www.amazon.in/s?k=english+quotes+t+shirts+for+men&crid=TIBZ9C9P45YJ&sprefix=t-shirt+with+english+quo%2Caps%2C422&ref=nb_sb_ss_ts-doa-p_1_24'
header={"user-agent":"Mozilla/5.0 (Windows NT ; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
req=requests.get(url,headers=header) #used to get info from the website
link=[]
soup=BeautifulSoup(req.text,'html.parser') #used to parse elements in the website
print(soup.title.text)

select=soup.select('img[src^="https://m.media-amazon.com/images"]')
for img in select:
    link.append(img['src'])

#for i in link:
    #print(i)
os.mkdir('shirt')

for index,img_link in enumerate(link):
    img_data=requests.get(img_link).content
    with open("shirt//"+str(index)+'.jpg','wb') as f:
        f.write(img_data)
    f.close()

