print("Hello World!")
print ("3.1")
x = "Goodbye World"
print (x) 
x = 6
print (x)
print (x + 3)
userinput = input("Type your name:")
userinput_len = len(userinput)
print (userinput_len)

if userinput_len > 5:
    print ("Length is greater than 5!")
    print ("Isn't that great!")
elif userinput_len == 5:
    print ("Length is equal to 5!")
    print ("That's still OK.")
else:
    print ("Length is less than or equal to 5!")
    print ("That's still OK.")

print ("End of program.")

myList = [1,1,2,3,5]

for number in myList:
    print (number)

for count in range(10):    #range from 0-9, always start at 0  
    if count == 3:
        print (count)
    else:
        print ("Not three")

def jared():
    for count in range(10):
        if count%2 == 0:
            print (count)
        else:
            print ("Odd.")

for count in range(10):
    if count%2 == 0:
        print (count)
    else:
        print ("Odd.")

print ("End of for loop :)")

jared()

f = open("file.txt")
count = 0
for letter in f.read():
    print (count, letter)
    count = count + 1
