import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from functions import make_cumulative
from functions import mad, mad2,mad3
from math import ceil

dataset=pd.read_csv('Flow (Total) - Thu 3rd Jan 2019 (Today).csv')

X= dataset.iloc[:,2].values
y= dataset.iloc[:,3].values
do= y-X
secs = do/1000
seconds=list(secs)
ga=[]
make_cumulative(secs,ga)

z=ceil(ga[-1]/3600)
necessary_list=[[val for idx,val in enumerate(ga) if 3600*level<val<=3600*(1+level)] for level in range(z)]

ram=[len(necessary_list[0])]
[ram.append(ram[i-1]+len(necessary_list[i])) for i in range(1,z)]
dlist=[ram[i] for i in range(z)]

dflist=[pd.DataFrame(dataset.iloc[0:dlist[0]])]
[dflist.append(pd.DataFrame(dataset.iloc[dlist[i-1]:dlist[i]])) for i in range(1,z)]

#####Making the dataset have hour breaks###
time=[]
dfnlist=[]
[dfnlist.append(mad(i,dlist,ga,seconds,time,dflist,dfnlist)) for i in range(z)]

#creating a new cumulative list that takes what happened above into account
cumula=[]
make_cumulative(seconds,cumula)
        
#creating the dataset with all of the datasets
dfx=pd.concat(dfnlist)
dfx.reset_index(drop=True,inplace=True)

#labelling the new dataset
dfx['Cumulative']=cumula
dfx['Second(s)']=seconds
dfx['Hour']=time

#drop unnecessary columns 
dfx.drop(['Start timestamp','Finish timestamp'],axis=1,inplace=True)

url_series=dfx['URL']
url_list=list(url_series)
title_series=dfx['Title']
titles=list(title_series)
pro1=0
un1=0
#domains and youtube paths that will be classified as productive work
prolist=[mad2(i,dlist,ga,seconds,url_list,pro1,un1) for i in range(z)]

unlist=[mad3(i,dlist,ga,seconds,url_list,pro1,un1) for i in range(z)]
int=[np.sum(prolist[i]+unlist[i]) for i in range(len(prolist))]

#creating the plot and productivity summary details
total_pro=np.add.reduce(prolist)
total_un=np.add.reduce(unlist)
total_time=total_pro+total_un
total_productivity=(total_pro/total_time)*100
jaja=[(prolist[i]/int[i])*100 for i in range(len(int))]
k=[jaja[i] for i in range(len(jaja)) if jaja[i]>=0]
unique=set(time)    
ut=list(unique)
plt.plot(ut,k, marker= 'o',label='Productivity per hour')
ax=plt.subplot()
plt.xlabel('Hour')
plt.ylabel('Productivity (%)')   
plt.title('Productivity over time')
ax.set_ylim([0,100])
plt.hlines(total_productivity, 1, z, colors='red', linestyles='solid', label='Average Productivity')
plt.legend()
ax.set_xticks(range(1,(len(unique)+1),1))
plt.savefig('Productivity over time 1.jpeg')
plt.show()
