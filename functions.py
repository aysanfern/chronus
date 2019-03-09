from urllib.parse import urlparse

#list of domains and paths
productive_domains=['drive.google.com','www.codecademy.com','www.udemy.com','www.superdatascience.com','docs.google.com','https://math.stackexchange.com','stackoverflow.com','github.com','scikit-learn.org','studentsunionucl.org']
productive_path=['v=eUfvyUEGMD8','v=PwhiWxHK8o','v=kVfhpn0EuhQ','v=uXt8qF2Zzfo']

#Make a cumulative list
def make_cumulative(list,newlist):
    new=0
    for i in range(len(list)):
        if i>0:   
            new= list[i]+newlist[i-1]
            newlist.append(new)
        else:
            newlist.append(list[0])
    return newlist


def mad(value,list_of_lengths,cumulative_list,seconds,time,dfhole,finom):
    if list_of_lengths[value]<len(cumulative_list) and cumulative_list[list_of_lengths[value]]>(3600* (value+1)):
        gino=3600*(value+1)-cumulative_list[list_of_lengths[value]-1]
        seconds.insert(list_of_lengths[value],gino)
        seconds[list_of_lengths[value]+(value+1)]=cumulative_list[list_of_lengths[value]]-3600*(1+value)
        if value>0:
            time+=((list_of_lengths[value]-list_of_lengths[value-1])+1)*[value+1]
        else:
            time+=(list_of_lengths[value]+1)*[value+1]
        ronald=dfhole[(value+1)]
        finom=dfhole[value].append(ronald.iloc[0])
        finom.reset_index(drop=True,inplace=True)
    else:
        if value>0:
            time+=((list_of_lengths[value]-list_of_lengths[value-1]))*[value+1]
        else:
            time+=(list_of_lengths[value])*[value+1]
        finom=dfhole[value]
    return finom

def mad2(value,dlist,cumulative_list,seconds,url_list,prolist,unlist):
    if (dlist[value])<=len(cumulative_list):
        if value>0:
            for i in range((dlist[value-1]+value),dlist[value]+(value)):
                temp=urlparse(url_list[i])
                if temp[1] in productive_domains:
                    prolist+=seconds[i]
                elif temp[4] in productive_path:
                    prolist+=seconds[i]
                else:
                    unlist+=seconds[i]
        else: 
            for i in range(0,dlist[value]+1):
                temp=urlparse(url_list[i])
                if temp[1] in productive_domains:
                    prolist+=seconds[i]
                elif temp[4] in productive_path:
                    prolist+=seconds[i]
                else:
                    unlist+=seconds[i]            
    return prolist


def mad3(value,dlist,cumulative_list,seconds,url_list,prolist,unlist):
    if dlist[value]<=len(cumulative_list):
        if value>0:
            for i in range((dlist[value-1]+value),dlist[value]+(value)):
                temp=urlparse(url_list[i])
                if temp[1] in productive_domains:
                    prolist+=seconds[i]
                elif temp[4] in productive_path:
                    prolist+=seconds[i]
                else:
                    unlist+=seconds[i]
        else: 
            for i in range(0,dlist[value]+(value+1)):
                temp=urlparse(url_list[i])
                if temp[1] in productive_domains:
                    prolist+=seconds[i]
                elif temp[4] in productive_path:
                    prolist+=seconds[i]
                else:
                    unlist+=seconds[i]

    return unlist
