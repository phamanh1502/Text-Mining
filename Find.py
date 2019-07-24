import os
import math
def Load_Data():
    data = []
    word_dict={}
    count = 0
    FJoin = os.path.join
    path = "Source"
    path_file = [FJoin(path, f) for f in os.listdir(path)]
    size = len(path_file)
    while(count<size):
        temp=Save_Data(path_file[count])
        data.append(temp)
        word_dict=set(word_dict)|set(data[count])
        count+=1
    return data,word_dict,path_file

def Save_Data(path):
    try:
        file = open(path)
        temp1 = file.read()
        temp2=temp1.split(" ")
        file.close()
    except FileNotFoundError:
        return
    return temp2

def Save_Value(data,word_dict):
    data_dict=[]
    size=len(data)
    count=0
    while(count<size):
        temp=dict.fromkeys(word_dict, 0)
        # count the word in bads
        for word in data[count]:
           temp[word] += 1
        data_dict.append(temp)
        count+=1
    return data_dict

def Calculate(data_dict,word_dict):
    size=len(data_dict)
    sum_word=dict.fromkeys(word_dict,0)
    #so van ban chua tu T
    for word in word_dict:
        for i in range(size):
            if(data_dict[i][word]>0):sum_word[word]+=1

    #so tu trong moi van ban
    for i in range(size):
        sum=0
        for word in word_dict:
            sum+=data_dict[i][word]
        for word in word_dict:
            f=float(data_dict[i][word])/float(sum)*math.log(float(size)/float(sum_word[word]))
            data_dict[i][word]=f
    return data_dict,sum_word

def Distance(word_dict,data_dict,main_dict):
    size=len(data_dict)-1
    array=[]
    for i in range(size):
        sum=0
        for word in word_dict:
            sum+=pow(data_dict[i][word]-main_dict[word],2.0)
        sum=pow(sum,1.0/2)
        array.append(sum)
    return array

def Find_Min(array):
    size=len(array)
    place=[0 for x in range(10)]
    for i in range(10):
        place[i]=i
    place=Sort(place,array)
    i=10
    while(i<size):
        place=Compare(place, array, i)
        i+=1
    return place
def Compare(place,array,pos):
    i=9
    while(i>1):
        if(array[place[9]]<array[pos]): break
        if(array[place[0]]>array[pos]):
            place.insert(0,pos)
            place.pop(10)
            return place
        elif array[pos]<array[place[i]] and array[pos]>array[place[i-1]]:
            place.insert(i,pos)
            place.pop(10)
            return place
        else: i-=1
    return place
def Sort(place,array):
    while(check_sort(place,array)):
        for i in range(9):
            if(array[place[i]]>array[place[i+1]]):
                a=place[i+1]
                place[i+1]=place[i]
                place[i]=a
    return place
def check_sort(place,array):
    for i in range(9):
        if(array[place[i]]>array[place[i+1]]): return True
    return False




