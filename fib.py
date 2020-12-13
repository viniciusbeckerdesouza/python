# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:06:00 2020

@author: souzavb
"""

def fib(n):
    """Gera uma série de fibonacci de n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Gera uma lista com a série de Fibonacci"""
    result = []
    a, b = 0, 1
    while a < n :
        result.append(a)
        a, b = b, a+b
    return result

f = fib2(100)
print(f)
