# FOR LOOPS EXERCISES

# Ex. 1
# Enter your name, save it in name variable and save in result_1 variable your name repeated 3 times (use loops)

name_1 = "Marina"
result_1 = name_1
for _ in range(2):
    result_1 += name_1
print(result_1)



# Ex. 2
# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then save in result_2 variable your name repeated as many times as number_1 is
# (use loops)
name_2 = "Marina"
number_1 = 6
result_2 = " "
for _ in range(number_1):
    result_2 += name_2
print(result_2)

# TODO: Here is your code


# Ex. 3
# Enter a random string, which includes only digits. Write code which find a sum of digits in this string and save it
# into result_3 variable

string_number_1 = "13485932"
result_3 = 0
for char in string_number_1:
    result_3 += int(char)
print(result_3)



# TODO: Here is your code


# Ex. 4
# Create code which sums up all even numbers between 2 and 100 (include 100) and save it in result_4 variable
result_4 = 0
for numbers in range(2, 101, 2):
    result_4 += numbers
print(result_4)

# TODO: Here is your code