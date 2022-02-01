# 1. create a bubble sort algorithm that sorts out 10 numbers in order

def bubble_sort(items: list):
    """
    Sort the items by swapping adjacent items if they are out of order
    """
    for n in range(len(items)):
        for k in range(len(items)-1):
            if items[k] > items[k+1]:
                items[k], items[k+1] = items[k+1], items[k]
    return items

arr = [64, 34, 25, 12, 22, 11, 90, 78, -1, -56, 67]
print(bubble_sort(arr))


# 2. create a list called "businessdays" that prints out only two days in all uppercase
def print_business_days(days: list):
    """
    Print out only two days in all uppercase
    """
    for day in days:
        if day.upper() == "MONDAY" or day.upper() == "TUESDAY":
            print(day.upper())

businessdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print_business_days(businessdays)

# 3. create an if statement that finds out if "sunday" is in the list. It will print an output of false
def is_sunday(days: list):
    """
    find out if "sunday" is in the list. It will print an output of false
    """
    for day in days:
        if day.upper() == "SUNDAY":
            print(False)
            break
    else:
        print(True)

is_sunday(businessdays)

# 4. create a class function that has a child class inherit from parent class
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs {self.price}"


class Book(Product):
    def __init__(self, name: str, price: float, author: str):
        super().__init__(name, price)
        self.author = author

    def __str__(self):
        return f"{self.name} by {self.author} costs {self.price}"

    
book = Book("The Art of Computer Programming", 100.00, "Donald Knuth")
print(book)

    





    







    
