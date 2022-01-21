# Create a while loop that prints a "L" shape object in stars 

# def star_pattern_letter_l():
#     """
#     Prints a "L" shape object in stars
#     """
#     counter = 0
#     while counter < 5:
#         print("*", ("*"*5 if counter == 4 else ""))
#         counter += 1
  


# star_pattern_letter_l()

# We have a report on the number of flu vaccinations in a class of 40 people. It has the following numbers: never:8 once: 10 twice: 4 Threetimes:6What is the mean number of the times those people have been vaccinated?

# students_class = 40
# never_vaccinated = 8
# once_vaccinated = 10
# twice_vaccinated = 4
# threetimes_vaccinated = 6

# mean_vaccinated = (never_vaccinated + once_vaccinated + twice_vaccinated + threetimes_vaccinated) / students_class

# Create a program that prints out prime numbers using the while loop.

counter = 2

prime_numbers = []
while counter < 100:
  if counter > 1:
      isPrime = True
  else:
      isPrime = False
  i = 2
  while i < counter:
    if counter % i == 0:
      break
    i += 1
  
  if isPrime:
      prime_numbers.append(counter)
counter += 1

print(prime_numbers)
    