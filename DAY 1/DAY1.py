# https://adventofcode.com/2023/day/1
import regex as re

s = 0
with open("list.txt", "r") as file:
    for line in file:
        temp = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        temp = [element.replace('one', '1')  for element in temp]
        temp = [element.replace('two', '2')  for element in temp]
        temp = [element.replace('three', '3')  for element in temp]
        temp = [element.replace('four', '4')  for element in temp]
        temp = [element.replace('five', '5')  for element in temp]
        temp = [element.replace('six', '6')  for element in temp]
        temp = [element.replace('seven', '7')  for element in temp]
        temp = [element.replace('eight', '8')  for element in temp]
        temp = [element.replace('nine', '9')  for element in temp]

        print (temp)
        if (len(temp) == 1):
            temp = temp[0] + temp[0]
        dig = temp[::len(temp)-1]
        print(dig)
        dig = dig[0] + dig[1]
        s = s + int(dig)
        print (s)
print('The total sum is:', s)
