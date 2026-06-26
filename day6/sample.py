#write a python program in oder to read csv file and copy the content in other file and copy other file
import csv 
f1=open("file1.csv","r")
data=csv.reader(f1)
for i in data:
    print(i)
f2=open("file")