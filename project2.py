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
        list.append(line.split("- ")[1])

def song_inforamtion(line,dict):

      if line.__contains__("name"):
        dict.update({"name":line.split(": ")[1]})

      if line.__contains__("singer"):
        dict.update({"singer":line.split(": ")[1]})

      if line.__contains__("genre"):
        dict.update({"genre":line.split(": ")[1]})

      if line.__contains__("tracks"):
        dict.update({"tracks":int(line.split(": ")[1])})

def find_user_index(id,a,user_info):
    if id=='1' or id=='2':
        for i in range(len(user_info)):
            if user_info[i]['name']==a:
                return i
    if id=='3' or id=='4':
        for i in range(len(user_info)):
            if user_info[i]['age']==int(a):
                return i
    if id=='5' or id=='6':
        for i in range(len(user_info)):
            if user_info[i]['city']==a:
                return i
    return -1

def find_album_index(id,b,song_info):
    list_of_index=[]

    if id=='1' or id=='3' or id=='5':
       for i in range(len(song_info)):
            if song_info[i]['singer']==b:
                    list_of_index.append(i)

    if id=='2' or id=='4' or id=='6':
        for i in range(len(song_info)):
            if song_info[i]['genre']==b:
                list_of_index.append(i)

    if len(list_of_index)>0:
        return list_of_index
    else:
        return [-1]

def check_request(albums_sold,list_of_index,song_info):
    the_number_of_songs_sold=0
    for it in albums_sold:
        for i in list_of_index:
            if song_info[int(i)]['name']==it:
                the_number_of_songs_sold+=song_info[i]['tracks']

    return the_number_of_songs_sold

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

    index=find_user_index(id,a,user_info)

    albums_sold=user_info[index]["albums"]

    list_of_index=find_album_index(id,b,song_info)



    if index==-1 or list_of_index.__contains__(-1):
        print(0)
    else:
       print(check_request(albums_sold,list_of_index,song_info))
