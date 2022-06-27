# import json
# def  movie_directors():
#     file2=open("Task5.json","r")
#     h=json.load(file2)
#     list=[]
#     for i in h:
#         if i["Genre:"]not in list:
#             list.append(i["Genre:"])
#     dict8={}
#     list9=[]
#     for k in list:
#         i=0
#         count=0
#         while i<len(h):
#             if k==h[i]["Genre:"]:
#                 count+=1
#             i+=1
#         dict8.update({k:count})
#     list9.append(dict8)
#     with open("Task11.json","w")as file:
#         json.dump(list9,file,indent=4)
#     return list9
# movie_directors()



# from WS_task5 import data
# import json

# def analyse_movie_gener(movie_list):
#     gener_list=[]
#     for movie in movie_list:
#         json_2_dic=json.loads(movie)
#         gener=json_2_dic["Genre:"]
#         for i in gener:
#             if i not in gener_list:
#                 gener_list.append(i)
#         print(gener_list)
#     analyse_gener={gener_type:0 for gener_type in gener_list}
#     for gener_type in gener_list:
#         for movie in movie_list:
#             json_2_dic=json.loads(movie)
#             if gener_type in json_2_dic["Genre:"]:
#                 analyse_gener[gener_type]+=1
#         print(analyse_gener)        
#         with open("Task11.json","w") as file:
#             json.dump(analyse_gener,file,indent=4)
#     return analyse_gener
# gener_analysis=analyse_movie_gener(data(movies=9))
# print(gener_analysis)








# from WS_task5 import data
# import json
# def  movie_directors():
#     list1=[]
#     count=0
#     for i in data:
#         gener=i["Genre:"]
#         for j in gener:
#             if j not in list1:
#                 list1.append(i["Genre:"])
#             print(j)
#             count+=1
# movie_directors()









# from WS_task5 import data
# import json

# def analyse_movie_gener(movie_list):
#     gener_list=[]
#     for movie in movie_list:
#         json_2_dic=json.loads(movie)
#         gener=json_2_dic["Genre:"]
#         for i in gener:
#             if i not in gener_list:
#                 gener_list.append(i)
#         print(gener_list)
#     analyse_gener={gener_type:0 for gener_type in gener_list}
#     for gener_type in gener_list:
#         for movie in movie_list:
#             json_2_dic=json.loads(movie)
#             if gener_type in json_2_dic["Genre:"]:
#                 analyse_gener[gener_type]+=1
#         print(analyse_gener)        
#         with open("Task11.json","w") as file:
#             json.dump(analyse_gener,file,indent=4)
#     return analyse_gener
# gener_analysis=analyse_movie_gener(data(movies=9))
# print(gener_analysis)








# import json

# file2=open("Task5.json","r")
# h=json.load(file2)
# def  movie_directors(h):
#     list1=[]
#     list2=[]
#     for i in h:
#         a=i["Genre:"].split()
#         for k in a:
#             if k[-1]==",":
#                 k=k[:-1]
#             list1.append(k)
#     for i in list1:
#         if i not in list2:
#             list2.append(i)
#     dict={}
#     for i in list2:
#         k=0
#         count=0
#         while k<len(list1):
#             if i==list1[k]:
#                 count+=1
#             k+=1
#         dict.update({i:count})
#     with open("Task11.json","w")as file:
#         json.dump(dict,file,indent=4)
# movie_directors(h)



from WS_task5 import data
import json

def movie_gener():
    list1=[]
    dict1={}
    for i in data:
        gener=i["Genre:"].split(",")
        for i in gener:
            list1.append(i)
            print(list1)                                                                        
        count=0
        for j in list1:
            count+=1
        dict1.update({j:count})
    with open("Task11.json","w") as file:
        json.dump(dict1,file,indent=4)
movie_gener()




