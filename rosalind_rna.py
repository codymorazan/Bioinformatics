# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:18:41 2020

@author: Corndog Expert
"""
#Problem link:   http://rosalind.info/problems/rna/

data = open("C:\\Users\\Corndog Expert\\Documents\\Python Scripts\\Personal Sets and Work\\Rosalind datasets\\rosalind_rna.txt").read().replace(" ", "")
rna = ""
for i in data:
    if i == "T":
        rna += "U"
    else:
        rna += i
print(rna)