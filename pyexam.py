# You need to calculate the points earned by a soccer team.
# The team won 18 games and ended 7 games as a draw.
# A win brings 3 points, while a draw brings 1.
# Create a program to calculate and output the total points earned by the team.
def total_points():
    games_won = 18
    games_draw = 7
    points_won = 3
    points_draw = 1
    total_points = games_won * points_won + games_draw * points_draw
    return total_points


print(total_points())

# Ever wondered how many seconds there are in a month (30 days)?

# Write a program to calculate and output the answer.
def seconds_in_month():
    days_in_month = 30
    seconds_in_day = 24 * 60 * 60
    seconds_in_month = days_in_month * seconds_in_day
    return seconds_in_month


print(seconds_in_month())

# Write a program that will multiply the sum of 5 and 6 by 57.3 and output the result.
def multiply_sum():
    sum_of_5_and_6 = 5 + 6
    result = sum_of_5_and_6 * 57.3
    return result


print(multiply_sum())


# You need to calculate the flight time of an upcoming trip. 
# You are flying from LA to Sydney, covering a distance of 7425 miles, 
# the plane flies at an average speed of 550 miles an hour.

# Calculate and output the total flight time in hours.

# Hint
# The result should be a float.

def flight_time():
    miles_traveled = 7425
    miles_per_hour = 550
    hours_per_mile = 1 / miles_per_hour
    flight_time = miles_traveled * hours_per_mile
    return flight_time


print(flight_time())
