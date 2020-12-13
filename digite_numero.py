# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:04:56 2020

@author: souzavb
"""

x = int(input("Digite um número: "))
if x < 0:
    x = 0
    print('Valor negativo.')
elif x == 0:
    print('Zero.')
elif x == 1:
    print('Uno.')
else:
    print('Mais.')
    