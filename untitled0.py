# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wPpHbpGTpWIr9FMoAR34tO5eUwmr7tvW
"""

x = 0 
while x < 10: 
    print("hello")
    x = x + 1

times = 0 
while times < 10: 
    times = times + 1 
    print("這是第", times, "次的hello")

times = 0
left = 0 
while times < 10: 
    times = times + 1 
    print("這是第", times, "次的hello")
    left = 10 - times 
    print("還有", left, "次機會")

sum = 0
i = 0
while sum <= 1000:
    i += 1
    sum += i*i
print('最小的n值為', i)

sum = 0 
x = 1 

while x < 11: 
    sum = sum + x 
    x = x + 2
    
print("1 + 3 + 5 + 7 + 9 = ", sum)