import requests

def create_tuple():
    try:
        products = tuple(requests.get('https://hub.dummyapis.com/products?noofRecords=10&idStarts=1001&currency=usd').json())

        print(type(products))
        counter =  0
        while counter != len(products):
            print(f'{products[counter]["name"]} ==> {products[counter]["price"]}')
            counter += 1
    except:
        print('Error, something went wrong')
        
print("============= TUPLE ===================\n")
create_tuple()
# 2. using list comprehension, print out odd numbers only
def odd_numbers(n):
    return [x for x in range(n) if x % 2 != 0]

print("============= LIST COMPREHENSION ODD NUMBERS ===================\n")
odd = odd_numbers(10)
for i in odd:
    print(i)

# 3. create a nesting list that prints 1 list all in upper case and 2 list all in lower case
def create_nesting_list():
    lst = [['a', 'b', 'c'], ['d', 'e', 'f']]
    
    for i in lst:
        for j in i:
            print(j.upper())
        for k in i:
            print(k.lower())

print("============= NESTING LISTS ===================\n")
create_nesting_list()

# 4. create a if, elif and else statement using the user input that prints
# "This is an odd number"(when it is odd) and "This is an even number"(when it is even)
# in a range of 10 and then the last statement prints "Done!"

def is_even_odd():
    num = int(input("Enter a number: "))
    for num in range(10):
        if num % 2 == 0:
            print(f"This is an even number {num}")
        else:
            print(f"This is an odd number {num}")
    print("Done!")

print("============= ODD EVEN NUMBERS ===================\n")
is_even_odd()

# 5. create two lists and combine them into one list then print all items using a for loop

def merge_lists():
    # get products
    products = requests.get('https://hub.dummyapis.com/products?noofRecords=10&idStarts=1001&currency=usd').json()

    product_names = []
    for product in products:
        product_names.append(product['name'])

    # get 10 users
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    
    user_names = []
    for user in users:
        user_names.append(user['name'])

    print(product_names)
    print(user_names)

    # combine the two lists
    merged_list = user_names + product_names

    # loop and print
    for post_user in merged_list:
        print(post_user)

print("============= MERGING LISTS ===================\n")
merge_lists()
    
