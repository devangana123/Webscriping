import json
from WS_task12 import movie_cast

def actor():
    with open("Task1.json","r") as file:
        data=json.load(file)
    final={}
    for i in data[:10]:
        cast_data=movie_cast(i["movie URL"])
        # print(cast_data)
        for k in cast_data:
            # print(k)
            if k["link"] not in final:
                final[k["link"]]={"name":k["name"],"frequent_co_actors":[]}
                for j in cast_data:
                    if k["link"]==j["link"]:
                        continue
                final[k["link"]]["frequent_co_actors"].append({
                    "imdb_id":k["link"],
                    "name": k["name"],
                    "num_movies": 1

                })
            else:
                for j in cast_data:
                    if k["link"]==j["link"]:
                        continue
                    for h in final[k["link"]]["frequent_co_actors"]:
                        if h["link"]==j["link"]:
                            h["num_movies"]+=1
                            break
                    else:
                        final[k["link"]]["frequent_co_actors"].append({
                            "imdb_id":j["link"],
                            "name": j["name"],
                            "num_movies": 1

                        })
    with open("Task14.json","w") as file:
        json.dump(final,file,indent=2)

actor()



