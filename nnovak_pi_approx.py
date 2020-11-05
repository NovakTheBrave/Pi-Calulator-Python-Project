# Nicholas Novak
# Python course code sample

import random 
import math


# This activity used a random library to approximate pi using a combined monet carlo and unifrom distribution approach.
# To do so, a circle will be inscribed within a square with sides K. This circle will then have a diameter of K.

# Next, N tuples are generated as (x,y) coordinate pairs. Using these tuples, the approximate shape of the circle can be found based on which tuples lie within the circle,
# which is centered at (0,0). Finally, using the approximate circle shape, pi can be backed out.



def inCircle(x_coord,y_coord,circle_radius):
    
    if math.sqrt((x_coord**2)+(y_coord**2))<=circle_radius:
        return True
    else:
        return False


#true
inCircle(math.sqrt(2)/2,math.sqrt(2)/2,1)

#false
inCircle(.8,.8,1)



# This part creates a list of n (x,y) tuples where if n=10, there will be n tuples where each value in the tuple ranges from -1 to 1 for a circle with diameter 1.


def random_tuple_creator(n):
    two_pole_list = []
    for i in range(n):
        tp_1 = random.uniform(-1,1)
        tp_2 = random.uniform(-1,1)
        two_pole = (tp_1,tp_2)
        two_pole_list.append(two_pole)
    return(two_pole_list)



random_tuple_creator(10)


# ## This function will determine the value of Pi
# 
# The input to the function will be the generated list of tuples.  
# Next each of those points will be used to determine if the tuple was within the circle or not. 
# Also, the total number of points in the circle and the total number of points overall will be tracked.




#Nicholas Novak Pi calculator sample code

#Import necessary functions
import random 
import math


#This first function is used to detect if a set of points lies within a given circle radius.
def inCircle(x_coord,y_coord,circle_radius):
    
    if math.sqrt((x_coord**2)+(y_coord**2))<=circle_radius:
        return True
    else:
        return False


def random_tuple_creator(n):
    two_pole_list = []
    for i in range(n):
        tp_1 = random.uniform(-1,1)
        tp_2 = random.uniform(-1,1)
        two_pole = (tp_1,tp_2)
        two_pole_list.append(two_pole)
    return(two_pole_list)


def piApproximation(tuple_list):
#Both random_tuple_creator and in_circle are inhereted to create this function
    final_list = []
    points_in = 0
    total_points = 0
    for i in tuple_list:
        total_points += 1
        x = ""
        y = ""
        x = i[0]
        y = i[1]
        if inCircle(x,y,1) == True:
            points_in += 1
            final_list.append(i)
    pie = (points_in*4)/total_points
    return(pie)
    
    pass





piApproximation(random_tuple_creator(100000))
