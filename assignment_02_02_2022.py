# 1. create a bubble sort algorithm using a while loop

def while_bubble_sort(items: list) -> list:
    """
    Sort the items by swapping adjacent items if they are out of order
    """
    while True:
        swapped = False
        for k in range(len(items)-1):
            if items[k] > items[k+1]:
                items[k], items[k+1] = items[k+1], items[k]
                swapped = True
        if not swapped:
            break
    return items

arr = [64, 34, 25, 12, 22, 11, 90, 78, -1, -56, 67]
print(while_bubble_sort(arr))

# 2. Create a numpy array using a function that prints out how many dimension is your array.

def numpy_array(items: list):
    """
    Create a numpy array using a function that prints out how many dimension is your array.
    """
    import numpy as np
    print(np.array(items).ndim)


two_dim_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numpy_array(two_dim_arr)

# 3.Create a 6-D array and reshape it to another size.
def reshape_array(items: list):
    """
    Create a 6-D array and reshape it to another size.
    """
    import numpy as np
    arr = np.array(items)
    
    # reshape 6-D array to 2-D array
    arr = arr.reshape(3, 2, 3)
    print(arr)


six_dim_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
reshape_array(six_dim_arr)

# 4. Create a forloop that prints your name 5 times.
def print_name(name: str):
    """
    Create a forloop that prints your name 5 times.
    """
    for i in range(5):
        print(name)

print_name("Iden")

# 5. Create a list and convert it back into a tuple.
def list_to_tuple(items: list) -> tuple:
    """
    Create a list and convert it back into a tuple.
    """
    return tuple(items)


list_arr = [1, 2, 3, 4, 5, 6]
print(list_to_tuple(list_arr))