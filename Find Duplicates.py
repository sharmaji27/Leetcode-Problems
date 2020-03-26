# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:41:08 2020

@author: sharma ji
"""

a = [3,3,3,3]
result = set()

for i in a:
    if a[abs(i)-1] > 0:
        a[abs(i)-1] *= -1
    
    else:
        result.add(abs(i))

print(list(result))