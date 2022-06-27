from WS_task1 import adventure_movie
from WS_task2 import group_by_year
import json

dec_arg=adventure_movie()
new_arg=group_by_year(dec_arg)
def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:
        mod=index%10
        decade=index-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()      
    for i in list1:
        moviedec[i]=[]

    for i in moviedec:
        dec10=i+9
        for x in movies:
            if x<=dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
        with open("Task3.json","w") as file:
            json.dump(moviedec,file,indent=4)
    return moviedec
print(group_by_decade(new_arg))
