# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:19:39 2020

@author: souzavb
"""

p = ['gato', 'janela', 'apartamento']
for i in p:
    print(i, len(i))

for i in range(len(p)):
    print(i, p[i])


for num in range(20):
    if num%2==0:
        print('É par: ', num)
        continue
    print('É ímpar: ', num)
    
while True:
    pass