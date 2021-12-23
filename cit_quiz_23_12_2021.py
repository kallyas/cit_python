# Track = [4.1,5.1,4.5,4.9,5.6,7.5,8.5,] Find the mode value in this list using a function. *
Track = [4.1,5.1,4.5,4.9,5.6,7.5,8.5,]
def mode(Track):
    mode = max(set(Track), key=Track.count)
    return mode
print(mode(Track))

# What gets printed? names1 = ['Amir', 'Barry', 'Chales', 'Dao'] loc = names1.index("Edward") print loc 
names1 = ['Amir', 'Barry', 'Chales', 'Dao']
# loc = names1.index("Edward")
# print(loc)
#
# What gets printed? class NumFactory: def __init__(self, n): self.val = n def timesTwo(self): self.val *= 2 def plusTwo(self): self.val += 2 f = NumFactory(2) for m in dir(f): mthd = getattr(f,m) if callable(mthd): mthd() print f.val *

# Which of the following will print the number of 'A' in the word: "HOW ARE YOU"? word = "HOW ARE YOU"? *
word = "HOW ARE YOU"
print(word.count('A'))

# In Python, what do you get when you multiply 23.0 by 4? Also, what kind of data/object type is it? 
print(23.0 * 4)
print(type(23.0 * 4))

# Using the magic method in a class function, print out 6 and 10. *
class Magic:
    def __init__(self):
        self.print_six_ten()
    
    def print_six_ten(self):
        print(6)
        print(10)

six_ten = Magic()

# ("Dave", "Jamie", "Jill", "Brenda") Which answer prints out Jamie? Pick Two
names = ("Dave", "Jamie", "Jill", "Brenda")
print(names[1])
print(names[-3])

# Refer to the the code: a_list = [10, 20, 30, 40]. What is the value of a_list[-1]? 
a_list = [10, 20, 30, 40]
print(a_list[-1])

# Study the code given below: import random x = random.randint(1,6) y = random.randint(1,6) z = random.randint(1,6) a = x + y + z What is the possible range of values for a? 
import random
x = random.randint(1,6)
y = random.randint(1,6)
z = random.randint(1,6)
a = x + y + z
print(a)

# What's the output of this code? Print(20 + 10 ** 2) *
print(20 + 10 ** 2)

# Create a 6 Dimensional array.
def six_dim_array():
    array = [[[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]], [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]], [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]], [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]], [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]], [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]]
    return array

print(six_dim_array())

# Which of the following function convert a String to a tuple in python?
string = "Hello"
print(tuple(string))
print(string.split())