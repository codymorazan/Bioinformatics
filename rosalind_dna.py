# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:37:21 2020

@author: Corndog Expert
"""

#Problem Link http://rosalind.info/problems/dna/

dna = open('C:\\Users\\Corndog Expert\\Documents\\Python Scripts\\Personal Sets and Work\\Rosalind datasets\\rosalind_dna.txt', 'r').read().rstrip('\n')

for i in 'ACGT':
    print(dna.count(i))