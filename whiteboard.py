# Define a make_chocolate function that takes in (in order) small, big, goal
# The goal is the Total number of lbs of Chocolate you want to receive
# big is the number of large pieces of chocolate you have available
# big chocolate weighs 5 pounds
# small is the number of small pieces of chocolate you have available
# small chocolate weights 1 pounds
# We want to use as many large bars of chocolate as possible to reach our Goal weight
# the Function should return the number of small
# pieces of chocolate you need to use to reach your goal



def solution(small, big, goal):
    big_chocolate = 5
    
    if goal//big_chocolate <= big:
        left_over=goal - (goal//big_chocolate*5)
    elif goal//big_chocolate > big:
        left_over=goal - big *5
 
    if left_over<=small:
        return left_over
    else:
        return -1