f = open("bumps_on_a_log_2.txt")

count = 1

for x in range(1,30) :
    print (f.read(1), end ="")
    f.read(count)
    count = count * 2