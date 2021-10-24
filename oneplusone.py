f = open("one_plus_one_equals_flag.txt")
content = f.readline()
pos = 0   ##position
inc = 1   ##increment
while pos < len(content) :
    print(content[pos], end ="")
    pos = pos + inc
    inc = inc + 1
    
    





