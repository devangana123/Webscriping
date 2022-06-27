

# from bs4 import BeautifulSoup
# import requests
# import json

# movie_details=[]
# def details_movie(link):
#     d1={}
#     link1=requests.get(link)
#     # print(link1)
#     soup=BeautifulSoup(link1.text,'html.parser')
#     # print(soup)
#     d1['name']='BlackPanther'
#     movie_bio=soup.find('div',class_='movie_synopsis clamp clamp-6 js-clamp' ).get_text().strip()
#     # print(movie_bio)4 
#     d1['Bio']=movie_bio
#     title=soup.find_all('div',class_='meta-label subtle')

#     value=soup.find_all('div',class_='meta-value')

#     for i in range(len(title)):
#         d1[str(title[i].get_text().strip())[:-1]]=value[i].get_text().strip()
#     movie_details.append(d1)

#     with open("Task4.json","w") as file:
#         json.dump(movie_details,file,indent=4)

# details_movie('https://www.rottentomatoes.com/m/black_panther_2018')




from WS_task1 import data
from bs4 import BeautifulSoup
import requests
import json

movie_details=[]
def details_movie(link):
    d1={}
    link1=requests.get(link)
    soup=BeautifulSoup(link1.text,'html.parser')
    d1['name']=soup.find('h1').text
    movie_bio=soup.find('div',class_='movie_synopsis clamp clamp-6 js-clamp' ).get_text().strip() 
    d1['Bio']=movie_bio
    title=soup.find_all('div',class_='meta-label subtle')

    value=soup.find_all('div',class_='meta-value')

    for i in range(len(title)):
        d1[str(title[i].get_text().strip())[:-1]]=value[i].get_text().strip().replace("\n"," ")
    movie_details.append(d1)

    with open("Task4.json","w") as file:
        json.dump(movie_details,file,indent=4)
details_movie("https://www.rottentomatoes.com/m/black_panther_2018")
