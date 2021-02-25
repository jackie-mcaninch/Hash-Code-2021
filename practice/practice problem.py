# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:51:30 2021

This code was created for practice for Google's 2021 global Hash Code Challenge
qualification round. The practice theme was pizza delivery, and the goal of the
problem was to deliver pizza to groups of 2, 3, or 4, one pizza to a person.
However, the parameter to optimize is the total amount of unique ingredients in
a group order of pizza. Input specifies various choices of pizza to deliver to
the groups, but each one can only be used once. Output specifies which pizzas
will be delivered to the groups. For each group, the score is given by the 
square of the number of different ingredients on all pizzas, and total score is
the sum of all the group scores.

@author: Jackie McAninch
"""
import time

def pick_pizzas(num_pizzas, pizza_dict, freq):
    pizzas = [] #used to store result
    minfo = []*num_pizzas #lists smallest scores and indexes thereof
    
    #ANALYZE FREQUENCY OF EACH TOPPING
    if not freq:
        for pizza in pizza_dict.values():
            for i in range(1,len(pizza)):
                topping = pizza[i]
                if topping in freq:
                    freq[topping] = freq[topping]+1
                else:
                    freq[topping] = 1
    
    #CALCULATE RELATIVE UNIQUENESS SCORE FOR EACH PIZZA
    #(sum(number of occurences for each topping))/(amount of toppings)
    #lower score means more unique
    for pizza in pizza_dict.keys():
        score = 0
        toppings = pizza_dict[pizza]
        #TALLY SCORE
        for j in range(1,len(toppings)):
            score += freq[toppings[j]]
        score = int(score/len(toppings))
        #STORE RUNNING MINIMUMS
        for n in range(num_pizzas):
            if len(minfo) < num_pizzas:
                minfo.append([score, pizza])
                break
            elif minfo[n][0] > score:
                del minfo[-1]
                minfo.insert(n, [score, pizza])
                break
    for pizza in minfo:
        pizzas.append(pizza[1])
        #DECREMENT TOPPING FREQUENCY UPON DELETION
        tmp = pizza_dict[pizza[1]]
        for j in range(1,len(tmp)):
            freq[tmp[j]] -= 1
        pizza_dict.pop(pizza[1])
    return tuple(pizzas)


files = {"e"}#, "c", "d", "e"}

for file in files:
    start = time.perf_counter()
    #FILE CREATION
    if file== "a":
        f_in = open(file, "r")
    else:
        f_in = open(file+".in", "r")
    f_out = open(file+"_out.txt", "w")
    
    #PARSE LINE 1
    line1 = (f_in.readline()).split()
    num_pizzas = int(line1[0])
    num_groups = [line1[1], line1[2], line1[3]] #total groups of 2,3, and 4
    
    #INITIALIZE OUTPUT ARRAYS
    deliveries2, deliveries3, deliveries4 = set(),set(),set() #holds tuples of pizza IDs, NO REPEATS
    pizzas = {}         #keys will be pizza ID and values will be toppings
    topping_freq = {}   #used to keep track of how frequently each topping occurs
    
    #STORE ALL GIVEN DATA
    for i in range(num_pizzas):
        pizzas[i] = (f_in.readline()).split()
    
    #ASSESS ORDER TO PROCEED (WHICH SET OF GROUPS FIRST)
    rel_yields = [0,0,0]
    rel_yields[0] = int(num_groups[0])*2
    rel_yields[1] = int(num_groups[1])*3
    rel_yields[2] = int(num_groups[2])*4
    
    #CALL ALGORITHM
    for i in range(3):
        ptr = rel_yields.index(max(rel_yields))
        rel_yields[ptr] = 0
        for j in range(int(num_groups[ptr])):
            if (ptr==0 and len(pizzas)>=2):
                deliveries2.add(pick_pizzas(ptr+2, pizzas, topping_freq))
            elif (ptr==1 and len(pizzas)>=3):
                deliveries3.add(pick_pizzas(ptr+2, pizzas, topping_freq))
            elif (ptr==2 and len(pizzas)>=4):
                deliveries4.add(pick_pizzas(ptr+2, pizzas, topping_freq))
            else:
                break
    
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
    
    end = time.perf_counter()
    print(f"Runtime: {end-start:0.4f} seconds")
f_in.close()
f_out.close()
