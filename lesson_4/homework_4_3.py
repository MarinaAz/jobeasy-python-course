# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = "Hello , world!"
char_1 = "l"

index = 0
counter = 0

while index < len(string_1):
    if string_1[index] == char_1:
        counter += 1
    index += 1

result_1 = counter
print(result_1)


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 23456

index = 0
result_2 = 1
while index < len(str(number_1)):
    result_2 *= int(str(number_1)[index])
    index += 1
print(result_2)


# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 23456

index = len(str(number_2)) - 1
result_3 = ""

while index >= 0:
    result_3 += str(number_2)[index]
    index -= 1
print(result_3)