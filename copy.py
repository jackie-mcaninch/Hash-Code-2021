# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:04:18 2021

@author: jacki
"""

files = ["a", "b", "c", "d", "e", "f"]
files = ["d"]
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
    
    j_counter = 0
    dict = {}
    intersections = {}
    for n in range(i):
        intersections[n] = []
    pnames = []
    count = 0
    for tmp in range(s+v):
        
        b = 0 #start of street
        e = 0 #end of street
        streetname = ""
        l = 0 #time it takes a car to get from beginning of the street to the end
        
        p = 0 #num of streets the car wants to travel
         #Name of streets, Car starts at the end of the first street
        
        line = (f_in.readline()).split()
        
        #print(line)
        #EVALUATE SET OF STREETS
        if(line[1].isnumeric()):
            streetname = line[2]
            b = line[0]
            e = line[1]
            l = line[3]
            intersections[int(e)].append(streetname)
            j_counter+=1
            if streetname not in dict:
                dict[streetname] = [b,e,l]
        #EVALUATE SET OF CARS
        else:
            count = count + 1
            p = int(line[0])
            pnames.append([])
            for j in range(p):
                pnames[count-1].append(line[j+1])
    total = 0
    count = 0          
    for n in range(i):
        count += 1
        total += len(intersections[n])
    
    print("TOTAL APPENDS PERFORMED: "+str(j_counter))
    print("TOTAL ROAD ENDPOINTS: "+str(total))
    print("LENGTH OF INTERSECTIONS: "+str(count))
    print("AVERAGE ROADS PER INTERSECTION: "+str(total/count))
    #WRITE OUTPUT
    lst = []
    f_out.write(str(i)+"\n")             #write how many intersections to schedule
    for n in range(i):
        f_out.write(str(n)+"\n")         #write ID of intersection
        f_out.write(str(len(intersections[n]))+"\n")
        for street in intersections[n]:
            f_out.write(street+" 1\n")
        lst = []
        
        
f_in.close()
f_out.close()