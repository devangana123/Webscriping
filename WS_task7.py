import json
def  movie_directors():
    file2=open("Task5.json","r")
    h=json.load(file2)
    # print(y)
    list=[]
    for i in h:
        # print(y)
        # print(i["Original Language"])
        if i["Director:"]not in list:
            list.append(i["Director:"])
    dict1={}
    list2=[]
    for k in list:
        i=0
        count=0
        while i<len(h):
            if k==h[i]["Director:"]:
                count+=1
            i+=1
        dict1.update({k:count})
    list2.append(dict1)
    with open("Task7.json","w")as file:
        json.dump(list2,file,indent=4)
    print(list2)
movie_directors()