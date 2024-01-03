#!/usr/bin/python3
import random

number = random.randint(-1000, 1000)

if number < 0:
    last_digit = ((number * -1) % 10) * -1
else:
    last_digit = number % 10

output_message = "Last digit of {} is {} and is ".format(number, last_digit)

if last_digit > 5:
    output_message += "greater than 5"
elif last_digit == 0:
    output_message += "0"
else:
    output_message += "less than 6 and not 0"

print(output_message)
