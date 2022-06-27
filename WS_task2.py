from WS_task1 import adventure_movie
import json

scraped=adventure_movie()
def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dic={i:[] for i in years}
    for i in movies:
        year=i["year"]
        for x in movie_dic:
            if str(x)==str(year):
                movie_dic[x].append(i)

        with open("Task2.json","w") as data:
                json.dump(movie_dic,data,indent=4)
    return movie_dic
print(group_by_year(scraped))
