# import requests
# from WS_task12 import movie_cast
# from bs4 import BeautifulSoup
# import json

# def scrap_movie_details(link):
#     cast=(movie_cast(link))
#     # print(cast)
#     cast_movie_name={}
#     url=requests.get(link)
#     soup=BeautifulSoup(url.text,"html.parser")
#     cast_movie_name["movie_name"]=soup.find("h1").text
#     main=soup.find("div",class_="panel-body content_body")
#     imfortable=main.find("ul",class_="content-meta info")
#     rowtable=imfortable.find_all("li",class_="meta-row clearfix")
#     for i in rowtable:
#         cast_movie_name[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())
#     cast_movie_name["cast"]=cast
#     with open("Task13.json","w") as file:
#         json.dump(cast_movie_name,file,indent=4)
#     return cast_movie_name
# scrap_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")



import requests
from WS_task12 import movie_cast
from bs4 import BeautifulSoup
import json
from WS_task1 import data


cast_movie_list=[]
for i in data:
    url=i["movie URL"]
    def scrap_movie_details(link):
        cast=(movie_cast(link))
        # print(cast)
        cast_movie_name={}
        url=requests.get(link)
        soup=BeautifulSoup(url.text,"html.parser")
        cast_movie_name["movie_name"]=soup.find("h1").text
        main=soup.find("div",class_="panel-body content_body")
        imfortable=main.find("ul",class_="content-meta info")
        rowtable=imfortable.find_all("li",class_="meta-row clearfix")
        for i in rowtable:
            cast_movie_name[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())
            cast_movie_name["cast"]=cast
            cast_movie_list.append(cast_movie_name)
        with open("Task123.json","w") as file:
            json.dump(cast_movie_name,file,indent=4)
        return cast_movie_name
    scrap_movie_details(url)



