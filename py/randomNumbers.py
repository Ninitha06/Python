import random

# Print random numbers from [0,1) means 0 is included, 1 is not included.

for i in range(10):
    print(random.random())


# Generate random numbers from [3,7)
# Option 1 - allows us to customize our own random function

def my_random():
    #Random, scale, shift
    return 4 * random.random() + 3

for i in range(10):
    print(my_random())

#Option 2
for i in range(10):
    print(random.uniform(3, 7))
    

# both uniform and random follows Normal distribution method. so same can be achieved with normalvariate func

#Mean and Std Deviation - Mean is where the bell curve peaks, Std Deviation is how narrow or wide the curve expands

# Mean will be center value that is 5, std deviation is (min 3, max 7)2/2 equally split on both sides, so 1 - approx guess

for i in range(10):
    print(random.normalvariate(5, 1))
    
# Discrete Probability distribution - rolling of dice

for i in range(10):
    print(random.randint(1, 6))
    
# Random element from a list

options = ['rock', 'paper', 'scissors']

for i in range(10):
    print(random.choice(options ))