# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:04:18 2021

@author: jacki
"""
files = ["a", "b", "c", "d", "e"]

for file in files:
    #FILE CREATION
    #f_in = open(file+".txt", "r")
    f_out = open("testrun.txt", "w")
        
    #STORE ALL GIVEN DATA
    d=6 
    i=4 
    s=5 
    v=2 
    f=1000
    data = {"2 0 rue-de-londres 1",
    "0 1 rue-d-amsterdam 1",
    "3 1 rue-d-athenes 1",
    "2 3 rue-de-rome 2",
    "1 2 rue-de-moscou 3"}
        
    #WRITE OUTPUT
    lst = []
    f_out.write(str(i)+"\n")             #write how many intersections to schedule
    for n in range(i):
        f_out.write(str(n)+"\n")         #write ID of intersection
        for line in data:
            line = line.split()
            if line[1]==str(n):
                print("line[1] =", line[1])
                print("n =",n)
                lst.append(line[2])
        f_out.write(str(len(lst))+"\n")         #write number of incoming streets for intersection
        for street in lst:
            f_out.write(street+" 3\n")
        lst = []
            
            
        
    
    
f_in.close()
f_out.close()