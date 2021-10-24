f = open("I_fibbed.txt")
count = 0
x = 0
y = 1

print (f.read(2), end ="")
f.read(1)
 
for a in range(1,30) :
    print (f.read(1), end ="")
    count = x + y
    f.read(count)   
    x = y
    y = count 
