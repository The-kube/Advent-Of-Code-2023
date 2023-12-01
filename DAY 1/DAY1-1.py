# https://adventofcode.com/2023/day/1
import re

s = 0
with open("list.txt", "r") as file:
    for line in file:
    # Defining a string with numbers

        temp = re.findall(r'\d', line)
        if (len(temp) == 1):
            temp = temp[0] + temp[0]
        dig = temp[::len(temp)-1]
        dig = dig[0] + dig[1]
        s = s + int(dig)
        print (s)
print('The total sum is:', s)
