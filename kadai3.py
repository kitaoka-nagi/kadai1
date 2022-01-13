import numpy as np
import matplotlib.pyplot as plt

x = [1452,1796,1894,2584,2735,3447]
y = [3231,3747,3726,5853,8866,10913]
year = ["2014","2015","2016","2017","2018","2019"]

plt.figure(figsize=(6,4))
plt.scatter(x,y,s=100,c="pink",edgecolors="red")
plt.xlabel("オープンキャンパス参加者数(人)",fontsize=10,fontname="MS Gothic")
plt.ylabel("志願者数(人)",fontsize=10,fontname="MS Gothic")
plt.title("matplotlib",fontsize=15,fontname="MS Gothic")
for i,label in enumerate(year):
    plt.annotate(label,(x[i],y[i]))

plt.show()