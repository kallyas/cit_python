"""
1. create in pandas, the name of the rows will be car and sales the values
"""

import pandas as pd


def car_sales():
    car_saless = pd.DataFrame({"car": ["Volvo", "BMW", "Toyota"],
                              "sales": [10, 8, 6]})
    return car_saless


"""
2. Create a pandas series with 1-D array.
"""

def panda_series():
    panda_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    return panda_series


"""
3. After you create the rows for cars and values for sales add the dates.
"""

def add_dates():
    car_sales_ = car_sales()
    car_sales_.insert(1, "date", ["2020-01-01", "2020-01-02", "2020-01-03"])
    return car_sales_


def main():
    print(car_sales())
    print(panda_series())
    updated_car_sales = add_dates()
    print(updated_car_sales)


if __name__ == "__main__":
    main()