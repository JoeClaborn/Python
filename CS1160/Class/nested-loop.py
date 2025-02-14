# print hours and minutes

#for hour in range(24):
    #for minute in range(60):
        #print(f"{hour:02.0f}:{minute:02.0f}")

# print grid

max_x = 10
max_y = 7
max_z = 3
num = 1

for x in range(max_x):
    for y in range(max_y):
        print(f"{num}\t", end="")
        num += 0.5
        
    print("")
    
for x in range(max_x):
    for y in range(max_y):
        for z in range(max_z):
            print(f"{x} {y} {z}")
