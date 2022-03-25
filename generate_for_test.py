import random

string = ""
j = 0
for i in range(3000):
    num_1 = str((round(random.uniform(-100,100), 0)))
    num_2 = str((round(random.uniform(-100,100), 0)))
#   для деления
#    while num_2 == 0:
#        num_2 = str((round(random.uniform(-10000, 10000), 4)))

#   добавление нулей
    if (j < 300):
        num_2 = '0.0'
    j = j + 1

    string += num_1 + " " + num_2 + "\n"

with open("test.txt", "w") as f:
    f.write(string)