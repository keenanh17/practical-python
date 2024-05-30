# bounce.py
#
# Exercise 1.5

ball_height = 100 # Meters
num_bounces = 0
# next_height = (3/5) * ball_height

while num_bounces < 10 :
    num_bounces = num_bounces + 1  
    ball_height = (3/5) * ball_height
    print(num_bounces , round(ball_height , 4))
