#Create a Python file named lab_3-3.py
#Import the random module.
import random as chara

#Use the randint() function to generate a random integer between 1 and 100.
print(chara.randint(1,100))
#Compare your result with another classmate. What do you notice about the results? Write your answers as a comment.
    #They were difrent dispite the fact that we used the same code.
#Use the seed() function to set the random seed to a value that you and a classmate agree on.
chara.seed(2763)
#Use the randrange() function to generate an even number between 0 and 100. 
print(chara.randint(1,100))
#Compare your result with your classmate. What do you notice about the results? Write your answers as a comment.
    #We both got 46.
