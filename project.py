
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('Flow (Total) - Sun 6th Jan 2019 (Today).csv')
X= dataset.iloc[:,2].values
y= dataset.iloc[:,3].values
do= y-X
secs = do/1000
seconds=list(secs)

rah=[]
x=0
new=0
ga=[]
for i in range(len(secs)):
    if i>0:   
        new= secs[i]+ga[i-1]
        ga.append(new)
    else:
        ga.append(secs[0])


t=[]
u=[]
k=[]
b=[]
bi=[]
bit=[]
bitb=[]
bitc=[]
bitd=[]
for i in range(len(ga)):
    if ga[i]<=3600:
        t.append(i)
    elif ga[i]<=7200:
        u.append(i)
    elif ga[i]<=10800:
        k.append(i)
    elif ga[i]<=14400:
        b.append(i)
    elif ga[i]<=18000:
        bi.append(i)
    elif ga[i]<=21600:
        bit.append(i)
    elif ga[i]<=25200:
        bitb.append(i)
    elif ga[i]<=28800:
        bitc.append(i)
    elif ga[i]<=32400:
        bitd.append(i)
    elif ga[i]<=36000:
        bite.append(i)


v1=len(t)
v2=len(u)
v3=len(k)
v4=len(b)
v5=len(bi)
v6=len(bit)
v7=len(bitb)
v8=len(bitc) 

sum1=len(t)
sum2=sum1+len(u)
sum3=sum2+len(k)
sum4=sum3+len(b)
sum5=sum4+len(bi)
sum6=sum5+len(bit)
sum7=sum6+len(bitb)
sum8=sum7+len(bitc)
sum9=sum8+len(bitd)

df1=pd.DataFrame(dataset.iloc[:sum1])
df2=pd.DataFrame(dataset.iloc[sum1:sum2])
df3=pd.DataFrame(dataset.iloc[sum2:sum3])
df4=pd.DataFrame(dataset.iloc[sum3:sum4])
df5=pd.DataFrame(dataset.iloc[sum4:sum5])
df6=pd.DataFrame(dataset.iloc[sum5:sum6])
df7=pd.DataFrame(dataset.iloc[sum6:sum7])
df8=pd.DataFrame(dataset.iloc[sum7:sum8])
df9=pd.DataFrame(dataset.iloc[sum8:sum9])
#####Making the dataset have hour breaks###

time=[]
if sum1<len(ga) and ga[sum1]>3600:
    #this is to create another entry that fills the hour
    n1= 3600 - ga[sum1-1]
    seconds.insert(sum1,n1)
    #this is to adjust the first entry of the next hour so it's split between the hour before and the current hour
    n2=ga[sum1]-3600
    seconds[sum1+1]=n2
    #this is to create another entry in the hour column since you're going to have another entry
    time+=(v1+1)*[1]
    #this adds in the last entry of the original dataset twice
    df1n=df1.append(df1.iloc[-1])
    #this makes sure the indexes are reset
    df1n.reset_index(drop=True,inplace=True)
else:
    time+=v1*[1]
    df1n=df1
sum2

if sum2<len(ga) and ga[sum2]>7200:
    n3=7200- ga[sum2-1]
    seconds.insert(sum2+1,n3)
    n4=ga[sum2]-7200
    seconds[sum2+2]=n4
    time+=(v2+1)*[2]
    df2n=df2.append(df2.iloc[-1])
    df2n.reset_index(drop=True,inplace=True)
else:
    time+=v2*[2]
    df2n=df2
    
if sum3<len(ga) and ga[sum3]>10800:
    n5=10800 - ga[sum3-1]
    seconds.insert(sum3+2,n5)
    n6=ga[sum3] -10800
    seconds[sum3+3]=n6
    time+=(v3+1)*[3]
    df3n=df3.append(df3.iloc[-1])
    df3n.reset_index(drop=True,inplace=True)
else:
    time+=v3*[3]
    df3n=df3

if sum4<len(ga) and ga[sum4]>14400:
    n7=14400 -ga[sum4-1]
    seconds.insert(sum4+3,n7)
    n8=ga[sum4] -14400
    seconds[sum4+4]=n8
    time+=(v4+1)*[4]
    df4n=df4.append(df4.iloc[-1])
    df4n.reset_index(drop=True,inplace=True)
else:
    time+=v4*[4]
    df4n=df4
    
if sum5<len(ga) and ga[sum5]>18000:
    n9=18000 -ga[sum5-1]
    seconds.insert(sum5+4,n9)
    n10=ga[sum5] -18000
    seconds[sum5+5]=n10
    time+=(v5+1)*[4]
    df5n=df5.append(df4.iloc[-1])
    df5n.reset_index(drop=True,inplace=True)
else:
    time+=v5*[5]
    df5n=df5
    
if sum6<len(ga) and ga[sum6]>21600:
    n11=21600 -ga[sum6-1]
    seconds.insert(sum6+5,n11)
    n12=ga[sum6] -21600
    seconds[sum6+6]=n12
    time+=(v6+1)*[4]
    df6n=df6.append(df4.iloc[-1])
    df6n.reset_index(drop=True,inplace=True)
else:
    time+=v6*[4]
    df6n=df6



#creating a new cumulative list that takes what happened above into account
cumula=[]
for i in range(len(seconds)):
    if i>0:   
        jj= seconds[i]+cumula[i-1]
        cumula.append(jj)
    else:
        cumula.append(seconds[0])
        



#creating the dataset with all of the datasets
dfx=df1n.append(df2n).append(df3n).append(df4n).append(df5n).append(df6n)
dfx.reset_index(drop=True,inplace=True)

#labelling the new dataset
dfx['Cumulative']=cumula
dfx['Second(s)']=seconds
dfx['Hour']=time


#drop unnecessary columns 
dfx.drop(['Start timestamp','Finish timestamp','Path'],axis=1,inplace=True)


#plot time

#creating the data points of effeciency with productive time spent on exclusively udemy, https://www.superdatascience.com ,YT- How SVM (Support Vector Machine) algorithm works
url_series=dfx['URL']
url_list=list(url_series)
title=list(dfx['Title'])
pro1=0
un1=0
for i in range(sum1+1):
    if 'udemy' in url_list[i]:
        pro1+=seconds[i]
    elif 'superdatascience' in url_list[i]:
        pro1+=seconds[i]
    elif 'Support Vector Machine' in title:
        pro1+=seconds[i]
    else:
        un1+=seconds[i]

sum2
pro2=0
un2=0
for i in range(sum1+1,sum2+2):
    if 'udemy' in url_list[i]:
        pro2+=seconds[i]
    elif 'superdatascience' in url_list[i]:
        pro2+=seconds[i]
    elif 'Support Vector Machine' in title:
        pro2+=seconds[i]
    else:
        un2+=seconds[i]
pro3=0
un3=0
for i in range(sum2+2,sum3+3):
    if 'udemy' in url_list[i]:
        pro3+=seconds[i]
    elif 'superdatascience' in url_list[i]:
        pro3+=seconds[i]
    elif 'Support Vector Machine' in title:
        pro3+=seconds[i]
    else:
        un3+=seconds[i]
pro4=0
un4=0
for i in range(sum3+3,sum4+4):
    if 'udemy' in url_list[i]:
        pro4+=seconds[i]
    elif 'superdatascience' in url_list[i]:
        pro4+=seconds[i]
    elif 'Support Vector Machine' in title:
        pro4+=seconds[i]
    else:
        un4+=seconds[i]
pro5=0
un5=0
if sum5<len(ga):
    for i in range(sum4+4,sum5+5):
        if 'udemy' in url_list[i]:
            pro5+=seconds[i]
        elif 'superdatascience' in url_list[i]:
            pro5+=seconds[i]
        elif 'Support Vector Machine' in title:
            pro5+=seconds[i]
        else:
            un5+=seconds[i]
else:
    for i in range(sum4+4,len(seconds)):
        if 'udemy' in url_list[i]:
            pro5+=seconds[i]
        elif 'superdatascience' in url_list[i]:
            pro5+=seconds[i]
        elif 'Support Vector Machine' in title:
            pro5+=seconds[i]
        else:
            un5+=seconds[i]
pro6=0
un6=0

if sum6<len(ga):
    for i in range(sum5+5,sum6+6):
        if 'udemy' in url_list[i]:
            pro6+=seconds[i]
        elif 'superdatascience' in url_list[i]:
            pro6+=seconds[i]
        elif 'Support Vector Machine' in title:
            pro6+=seconds[i]
        else:
            un6+=seconds[i]
else:
    for i in range(sum5+5,sum6):
        if 'udemy' in url_list[i]:
            pro6+=seconds[i]
        elif 'superdatascience' in url_list[i]:
            pro6+=seconds[i]
        elif 'Support Vector Machine' in title:
            pro6+=seconds[i]
        else:
            un6+=seconds[i]
sum5
nissa=[]
int=[pro1+un1,pro2+un2,pro3+un3,pro4+un4,pro5+un5,pro6+un6]
effe=[pro1,pro2,pro3,pro4,pro5,pro6]
int[1]
len(effe)
for i in range(len(effe)):
    if int[i]>0:
        nissa.append(effe[i]/int[i])
unique=set(time)    
ut=list(unique)
plt.plot(ut,nissa)
plt.xlabel('Hour')
plt.ylabel('Productivity (%)')   
plt.title('Productivity over time')
plt.show()
