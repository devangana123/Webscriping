from bs4 import BeautifulSoup
import json
import requests
                                                                       
def movie_cast(movie_url):
    cast_list=[]
    data=requests.get(movie_url)
    soup=BeautifulSoup(data.text,"html.parser")
    tag=soup.find("div",class_="castSection")
    alltags=tag.find_all("div",class_="cast-item media inlineBlock")
    for i in alltags:
        link=i.find("a",class_="unstyled articleLink")
        link1=link["href"]
        # print(link1)
        name=i.find('span').get_text().strip()
        # print(name)
        cast_dict={}
        cast_dict["name"]=name
        cast_dict["link"]=link1#.split("/")[-1]
        cast_list.append(cast_dict)
    with open("Task12.json","w") as file:
        json.dump(cast_list,file,indent=4)
    return cast_list
data=movie_cast("https://www.rottentomatoes.com/m/black_panther_2018")


