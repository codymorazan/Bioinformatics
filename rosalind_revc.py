# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:02:23 2020

@author: Corndog Expert
"""

data = open("C:\\Users\\Corndog Expert\\Documents\\Python Scripts\\Personal Sets and Work\\Rosalind datasets\\rosalind_revc.txt").read().replace(" ", "")

complement = ""

for i in data[::-1]:
    if i == "A":
        complement += "T"
        continue
    if i == "T":
        complement += "A"
        continue
    if i == "G":
        complement += "C"
        continue
    if i == "C":
        complement += "G"
        continue

print(complement)