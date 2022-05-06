#FOR loop
n = 100 #condition of 100 means loop will run 100x

for i in range(1, n): #starting with 1 means will never reach 100, only 99.
    print(i)

#WHILE loop
i = -5

while i < 6:
    print(i) # will run indefinitely because 1 is always smaller than 6
i += 1 #loop will run the first iteration of 1 since 1 is less than 6