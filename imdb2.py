import json
# import pprint



f=open("C:\\Users\\LENOVO\\OneDrive\\Desktop\\python\\imdb_movies.json.json",mode='r')
movies_data=json.load(f)
# f.close()
# pprint.pprint(movies_data)

# question 1:
# dic={}
# for data in movies_data:
#     director=data['director']
#     movie=data['name']
#     if director not in dic:
#         dic[director] = 1
#     else:
#         dic[director]+=1
# data1=max(dic.items(), key=lambda x: x[1])[1]
# # print(data)
# for data in dic:
#     if dic[data]==data1:
#         print(data)


# question2:
# dic={}
# for data in movies_data:
#     genre=data['genre']
#     for j in genre:
        # if j.strip() not in dic: strip function  it removes unwanted spaces
#             dic[j.strip()]=1
#         else:
#             dic[j.strip()]+=1
# data=max(dic.items(), key=lambda x: x[1])
# print(data)


# question3:
# dic={}
# for data in movies_data:
#     movies=data["name"]
#     imdb_score= float(data["imdb_score"])
#     if movies not in dic:
#         dic[movies]=imdb_score
#         # print(movies,imdb_score)
# data1=sorted(dic.items(), key=lambda x: x[1],reverse=True)
# print(data1[: 10])

# question4:

# dic={}
# for data in movies_data:
#     movies=data["name"]
#     imdb_score= float(data["imdb_score"])
#     if movies not in dic:
#         dic[movies]=imdb_score
#         # print(movies,imdb_score)
# min1=min(dic.items(), key=lambda x: x[1])[1]
# print(min1)
# print([i for i, j in dic.items() if j == min1])

# or nak ardam kaledu paina line so nen chatgpt vadanu rasthe okke line lo rayochu or motham looping vadochu kinda vadinatu
# result = []                     # 1. start with an empty list
# for i, j in dic.items():        # 2. iterate over each (key, value) pair
    # if j == min1:               # 3. check the condition
        # result.append(i)        # 4. if true, add key to result
# print(result)                   # 5. print the final list

# print(data1[0])


# questin 5

# dic={}
# for data in movies_data:
#     director=["director"]
    

    
    
        

    




        

    



    


    
    




