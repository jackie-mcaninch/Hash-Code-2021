# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:04:18 2021

@author: jacki
"""

files = ["a", "b", "c", "d", "e", "f"]
files = ["a"]
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
    
    dict = {}
    pnames = []
    count = 0
    while True:
        
        b = 0 #start of street
        e = 0 #end of street
        streetname = ""
        l = 0 #time it takes a car to get from beginning of the street to the end
        
        p = 0 #num of streets the car wants to travel
         #Name of streets, Car starts at the end of the first street
        
        line = (f_in.readline()).split()
        if not line: #breaks loop if at end of file
            break
        
        #print(line)
        if(line[1].isnumeric()):
            streetname = line[2]
            b = line[0]
            e = line[1]
            l = line[3]
            if streetname not in dict:
                dict[streetname] = [b,e,l]
        else:
            count = count + 1
            p = int(line[0])
            pnames.append([])
            for j in range(p):
                pnames[count-1].append(line[j+1])
                
        print(dict)
        print("")
        print(pnames)
        
        
    
    
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

