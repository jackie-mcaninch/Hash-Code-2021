# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:04:18 2021

@author: jacki
"""
files = ["a", "b", "c", "d", "e"]

for file in files:
    #FILE CREATION
    f_in = open(file+".txt", "r")
    f_out = open(file+"_out.txt", "w")
    
    #PARSE LINE 1
    line1 = (f_in.readline()).split()
    num_pizzas = int(line1[0])
    num_groups = [line1[1], line1[2], line1[3]] #total groups of 2,3, and 4
        
    #STORE ALL GIVEN DATA
    for i in range(num_pizzas):
        pizzas[i] = (f_in.readline()).split()
        
    #WRITE OUTPUT
    f_out.write(str(len(deliveries2)+len(deliveries3)+len(deliveries4))+"\n")
    for deliv in deliveries2:                   #GROUPS OF 2
        f_out.write("2")
        for pizza in deliv:
            f_out.write(" "+str(pizza))
        f_out.write("\n")
    for deliv in deliveries3:                   #GROUPS OF 3
        f_out.write("3")
        for pizza in deliv:
            f_out.write(" "+str(pizza))
        f_out.write("\n")
    for deliv in deliveries4:                   #GROUPS OF 4
        f_out.write("4")
        for pizza in deliv:
            f_out.write(" "+str(pizza))
        f_out.write("\n")
    
f_in.close()
f_out.close()