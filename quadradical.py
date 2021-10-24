f = open("quad-radical.txt")

count = 0

for x in range(1,30) :
    print (f.read(1), end ="")
    f.read(count)
    count = x**2



