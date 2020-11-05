# Nicholas Novak
# Python course code sample

import random 
import math


# In this activity, we are going to work with the random library and approximate pi using a probabilistic approach (monte carlo combined with a uniform distribution).  While probability knowledge is certainly not a prerequistie for this class if you want a visual representation of what we are doing you can follow the logic below.  
# 
# We are going to take a square with sides K.  We are going to have a circle inscribed in the square with diamater K (and radius K/2)
# 
# $area_{square}=K^2$
# 
# $area_{circle}=\pi(\frac{K}{2})^2$
# 
# If we were to randomly generate a very large number N (x,y) coordinate pairs we might hope that the proportion of darts that fall within the red circle would be $proportion_{red circle} = \frac{\pi(\frac{K}{2})^2}{K^2}=\frac{\pi(\frac{K^2}{4})}{K^2}=\frac{\pi}{4}\approx 0.785$
# 
# Changing this problem slightly, lets say we didn't know what the value of $\pi$ was and we wanted to determine it through a monte carlo trial.
# 
# Using a uniform distribution we can approximate pi quite accurately!  A uniform distribution is one such that the probability is constant.  If a uniform distribution ranges from 0 to 10, the probability of a number being between 5 and 6 is the same as a number being between 0 and 1.  This is NOT true in a normal distribution (the bell curve caused by using the gaussian) popular amoung professors!
# 
# $proportion_{circle} = \frac{\pi}{4}$
# 
# $4*proportion_{circle} = \frac{\pi}{4}*4 = \pi$
# 
# 
# We will generate N tuples, and approximate pi!
# 
# We will simplify this mathematically by assuming our circle is centered at the origin, and the radius of the circle is 1.

# Your first task is to generate a function to check if a point falls within a circle with radius K (or on the boundary).  To simplify this lab, let's assume that the circle is centered at (0,0) in an x-y coordinate system.  I have provided a few test cases your function should pass before you move on.  If a point is within the circle return true, otherwise return false.  No need to worry about robust error handling here, just a simple return statement.  Let's pretend this is tennis and lines are in, so anything actually on the circle is considered in the circle.
# 


def inCircle(x_coord,y_coord,circle_radius):
    #your code here
    if math.sqrt((x_coord**2)+(y_coord**2))<=circle_radius:
        return True
    else:
        return False


#true
inCircle(math.sqrt(2)/2,math.sqrt(2)/2,1)

#false
inCircle(.8,.8,1)



##Create a list of n (x,y) tuples 
## if n=10, you'll have n tuples where each value in tuple needs to range from -1 to 1
## If you want to use zip, you can create 2 lists of random numbers and zip them together to get your tuples
## Make sure to cast that zip object to a list

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
# The input to the function will be that list of tuples.  Next you will need to use each of those points and determine if it's within the circle or not.  Keep track of the total number of points in the circle, and the total number of points.  To make things easy, merely loop through the input of this function and use your in circle check to keep track of the proportion in the circle.




#Nicholas Novak Pi calculator sample code

#Import necessary functions
import random 
import math


#This first function is created to detect if a set of points lies within a given circle radius.
def inCircle(x_coord,y_coord,circle_radius):
    #This function uses simple mathematics to 
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
#Use both random_tuple_creator and in_circle to create this function
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
