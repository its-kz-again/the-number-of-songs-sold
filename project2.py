import re

def user_information(line,list,dict):

    if line.__contains__("name"):
        dict.update({"name":line.split(": ")[1]})

    if line.__contains__("age"):
        dict.update({"age":int(line.split(": ")[1])})

    if line.__contains__("city"):
        dict.update({"city":line.split(": ")[1]})

    if line.__contains__("albums"):
        dict.update({"albums":list})

    if re.findall(r"^\s{4}",line):
        list.append(line.split("-")[1])

def song_inforamtion(line,dict):

      if line.__contains__("name"):
        dict.update({"name":line.split(": ")[1]})

      if line.__contains__("singer"):
        dict.update({"singer":line.split(": ")[1]})

      if line.__contains__("genre"):
        dict.update({"genre":line.split(": ")[1]})

      if line.__contains__("tracks"):
        dict.update({"tracks":int(line.split(": ")[1])})

def find_index(id,a,user_info):
    if not(user_info.__contains__(a)):
        return -1
    if id==1 or id==2:
        for i in range(len(user_info)):
            if user_info[i]['name']==a:
                return i
    if id==3 or id==4:
        for i in range(len(user_info)):
            if user_info[i]['age']==int(a):
                return i
    if id==5 or id==6:
        for i in range(len(user_info)):
            if user_info[i]['city']==a:
                return i

def check_request(id,a,b,user_info,song_info):
    index=find_index(id,a,user_info)




n=int(input())
list=[]
dict={}
user_info=[]
song_info=[]

while True:
    try:
        line = input()

        if dict.__contains__("name") and line.__contains__("name"):
            user_info.append(dict)
            dict={}
            list=[]

        if line.isdigit():
            user_info.append(dict)
            dict={}
            list=[]
            m=int(line)
            break

        user_information(line,list,dict)

    except:
        pass

while True:
    try:
       line=input()

       if dict.__contains__("name") and line.__contains__("name"):
            song_info.append(dict)
            dict={}

       song_inforamtion(line,dict)

       if line.isdigit():
            song_info.append(dict)
            dict={}
            q=int(line)
            break

    except:
        pass


for i in range(q):
    id,a,b=map(str,input().split())
