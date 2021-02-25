# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:04:18 2021

@author: jacki
"""
files = ["a", "b", "c", "d", "e", "f"]

for file in files:
    #FILE CREATION
    f_in = open("Input Files/"+file+".txt", "r")
    f_out = open(file+"_out.txt", "w")
    
    d = 0 #Duration of simulation in seconds
    i = 0 #number of intersections (with ids from 0 to i-1)
    s = 0 #number of streets
    v = 0 #number of cars
    f = 0 #bonus points for each car that reaches the destination before time D
    
    #PARSE LINE 1
    line1 = (f_in.readline()).split()
    print(line1)
    d = int(line1[0])
    i = int(line1[1])
    s = int(line1[2])
    v = int(line1[3])
    f = int(line1[4])
    print("\n"+file)
    print("Duration: " + str(d))
    print("Intersections: " + str(i))
    print("Streets: " + str(s))
    print("Cars: " + str(v))
    print("Bonus Points: " + str(f))
    
    """  
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
    """
f_in.close()
f_out.close()