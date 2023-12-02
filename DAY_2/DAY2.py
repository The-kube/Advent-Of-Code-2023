#https://adventofcode.com/2023/day/2

import re

n_red       = 0
n_green     = 0
n_blue      = 0
found       = 0
s_imp       = 0
s_all       = 0
s_pos       = 0
max_red     = 0
max_green   = 0
max_blue    = 0
power       = 0
s_power     = 0
with open("input.txt", "r") as file:
    for line in file:
        found = 0
    #input = 'Game 52: 12 blue, 8 red; 11 green, 91 red, 11 blue; 82 blue, 5 green, 8 red; 3 red, 11 blue, 11 green; 12 blue, 64 green, 5 red; 10 red, 82 green'
        split = line.split(":")
        game = split[0]

        game = int(re.findall(r'\d+', game)[0] )
        s_all = s_all + game
        string = split[1]
        string = string.split(";")
        #temp = re.findall(r'\d|red|green|blue', input)
        for i in range(len(string)):
            print (string[i])
            set = string[i].split(",")
            #print (set)
            
            for i in range(len(set)):
                
                #temp = re.findall(r'\d+|red|green|blue', set[i])
                print ("set", set)
                red     = re.findall(r'\d+ red'  , set[i])
                if red:
                    red = re.findall(r'\d+', red[0])
                    red = int(red[0])
                    if red > max_red:
                        max_red = red
                    print("max_red", max_red)
                    if (red > 12) and found == 0:
                        #print("impossible_red")
                        #print(game)
                        found = 1
                        s_imp = s_imp + game
                        #print("found_red", found)
                        #print("sum  partial", s_imp, game)
                green   = re.findall(r'\d+ green', set[i])
                if green:
                    green = re.findall(r'\d+', green[0])
                    green = int(green[0])
                    if green > max_green:
                        max_green = green
                    print("max_green", max_green)
                    if (green > 13) and found == 0:
                        found = 1
                        s_imp = s_imp + game
                blue    = re.findall(r'\d+ blue' , set[i])
                if blue:
                    blue = re.findall(r'\d+', blue[0])
                    blue = int(blue[0])
                    if blue > max_blue:
                        max_blue = blue
                    print("max_blue", max_blue)
                    #n_blue = n_blue + blue
                    if (blue > 14) and found == 0:
                        found = 1
                        s_imp = s_imp + game
                
                
                print ("red",    red)
                print ("green",  green)
                print ("blue",   blue)
        power = power + (max_red * max_green * max_blue)
        max_red = max_green = max_blue = 0
        print("power", power)
s_power = s_power + power
s_pos = s_all - s_imp

print ("sum",    s_imp, s_all, s_pos)
print("max_red", max_red)
print("max_green", max_green)
print("max_blue", max_blue)
print("power", power)
print("s_power", s_power)
