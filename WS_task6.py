import json
def  movie_directors():
    file2=open("Task5.json","r")
    h=json.load(file2)
    list=[]
    for i in h:
        if i["Original Language:"]not in list:
            list.append(i["Original Language:"])
    dict8={}
    list9=[]
    for k in list:
        i=0
        count=0
        while i<len(h):
            if k==h[i]["Original Language:"]:
                # print(k)
                count+=1
            i+=1
        dict8.update({k:count})
    list9.append(dict8)
    with open("Task6.json","w")as file:
        json.dump(list9,file,indent=4)
    return list9
movie_directors()