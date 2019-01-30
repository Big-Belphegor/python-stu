__author__ = "Alien"
import json

filename = 'number.json'
with open(filename) as file:
    numbers = json.load(file)

print(numbers)