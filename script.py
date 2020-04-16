import requests
import sys
import math
from os import rename


# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello,{}'.format(who_to_greet)
    return greeting


r = requests.get('https://google.com')
print(r.status_code)

name = input("Your name? ")
print('hello', name)


# command palette -> sort imports will sort imports by base / 3rd party / whatever and organizes it well

# linting -> when file is saved, will alert you to hard errors and inefficiencies, i.e. unused variables

# coderunner output/run is read-only, writes such as input will not work. run from terminal thru right
#   click instead
