# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 18:22:40 2021

@author: Adri Saha
"""
#problem no 1

list1=[]
for i in range(1, 1001):
    if (i%8==0):
        list1.append(str(i))
print (list1)

#%% problem no 2

list1=[]
for i in range (1 ,1001):
    list1.append(str(i))
    if list1[i-1].find('6')!=-1:
     print(list1[i-1])

#%%
#problem 3

string = "Practice Problems to Drill List Comprehension in Your Head."
print("String is : ", string)
n=len(string)
count=0

for i in range(1,n):
    if(string[i]==' '):
       count+=1 
print("Spaces of the string is : ",count)


#%% problem no 4

string = "Practice Problems to Drill List Comprehension in Your Head."
print("Before removing vowel : " ,string)
for word in string:
    if word in ('a','e','i','o','u','A','I','E','O','U'):
        string = string.replace(word, '')
print("After removing vowel :", string)

#%% problem no 5
 
string="Practice Problems to Drill List Comprehension in Your Head."
new=" "
st=string.split(new)

for i in range (1,len(st)):
    if(len(st[i])<5 ):
        print(st[i])


#%% problem no 6

string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()
word_lengths = []
for word in words:
   word_lengths.append(len(word))
print(words)
print(word_lengths)

#%% Problem no 7

list3=[]
for i in range (1,1001):
    for j in range(2,10):
        if (i%j)==0:
         list3.append(i)
print(list(set(list3)))


#%% problem no 8

highest={num: max([divisor for divisor in range(1,10) if num % divisor == 0]) 
         for num in range(1,1001)}
print(highest)
   
 
        



