import json
from WS_task5 import data


def movie_director2(movie_directer):
    dic={}
    for directer in movie_directer:
        directer=directer["Director:"]
        dic[directer]={}
        count=0
        for  directer1 in range(len(movie_directer)):
            if directer==movie_directer[directer1]["Director:"]:
                language=movie_directer[directer1]["Original Language:"]
                count+=1
                dic[directer].update({language:count})
    with open("Task10.json","w") as file:
        json.dump(dic,file,indent=4)
movie_director2(data)

        

