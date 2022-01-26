# 1. Create a class called "oddeven" that prints if a number is odd or even in a range of 20.

class OddEven:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def oddeven(self):
        for i in range(self.start, self.end):
            if i % 2 == 0:
                print(i, "is even")
            else:
                print(i, "is odd")


# 2. Create a class that uses a user input to print out your output.

class UserInput:
    def __init__(self):
        self.input = input("Enter a number: ")

    def userinput(self):
        print(f"user input is: {self.input}")

# 3. .Create a class that has 3 child classes that inherits from the parent class.

class Parent:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"Parent class name is: {self.name}")

class Child1(Parent):
    def __init__(self, name):
        super().__init__(name)

    def print_name(self):
        print(f"Child1 class name is: {self.name}")


class Child2(Parent):
    def __init__(self, name):
        super().__init__(name)

    def print_name(self):
        print(f"Child2 class name is: {self.name}")


class Child3(Parent):
    def __init__(self, name):
        super().__init__(name)

    def print_name(self):
        print(f"Child3 class name is: {self.name}")

# 4. Create a whileloop that is counting down from 10 to 1.

def countdown():
    i = 10
    while i > 0:
        print(i)
        i -= 1

def main():
    odd_even = OddEven(1, 20)
    odd_even.oddeven()

    user_input = UserInput()
    user_input.userinput()

    child1 = Child1("Child1")
    child2 = Child2("Child2")
    child3 = Child3("Child3")

    child1.print_name()
    child2.print_name()
    child3.print_name()

    countdown()



if __name__ == '__main__':
    main()