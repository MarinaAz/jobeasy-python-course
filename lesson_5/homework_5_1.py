# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

num_1 = 5
num_2 = 3
def dif_two_numbers(num_1, num_2):
   print(num_1 - num_2)

dif_two_numbers(num_1, num_2)


# Division
# Write a function, which will divide these two numbers

 def division(num_1, num_2):
    print(num_1 / num_2)

division(num_1, num_2)


# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10


def function_1(number: int):
    if number > 10:
        return 100 - number
    else:
        return number * 10



# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

def temperature_convertor(fahrenheit_degree: int):
    return round((fahrenheit_degree - 32) * 5/9, 2)

temperature_fahrenheit = int(input('What temperature is right now?: ' ))
print(temerature_convertor(temperature_fahrenheit))



# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

def taxi_fare(distance):
    return round(4.0 + ((distance * 1000) / 140) * 0.25, 2)

print(taxi_fare(10))

# examples of usage:
# taxi_fare(10) #21.86
