# Write your first program. Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula (32°F − 32) × 5/9 = 0°C
import math
# type your code here
temperature_fahrenheit = int(input("What's temperature right now?"))
result_temperature = (temperature_fahrenheit - 32) * 5/9
print(f'in Celsius it will be: {math.floor(result_temperature)}')
