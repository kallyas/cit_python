# You're making a calculator that should add multiple numbers taken from input and output the result. The number of inputs is variable and should stop when the user enters "stop"
def calculator():
    add = 0
    multiply = 1
    while True:
        num = input("Enter a number: ")
        if num == "stop":
            break
        else:
            add += int(num)
            multiply *= int(num)
    print("The sum is:", add)
    print("The product is:", multiply)


calculator()

# The given outputs A B C D (each letter is separated by a space). Modify the code to output each letter on a separate line, resulting in the following output.
def letter_output():
    for letter in "A B C D":
        # ignore the space
        if letter == " ":
            continue
        print(letter)
        

letter_output()

# You are given a program with two inputs: one as password and the second one as password repeat. "Complete" if password and repeat are equal, and output "wrong", if they are not.
def password_check():
    pass_1 = input("Enter password: ")
    pass_2 = input("Repeat password: ")
    if pass_1 == pass_2:
        print("Complete")
    else:
        print("Wrong")


password_check()

# Bonus Question: 
# Create a file called answersheet.txt and write your quiz answers 
# on that file.

def bonus_question():
    with open("answersheet.txt", "w") as file:
        questions = 21
        for i in range(questions):
            answer = input(f"Enter answer for question {i+1}: ")
            file.write(answer + "\n")


bonus_question()