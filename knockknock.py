import socket

server = "znjp.com"
port = 31337
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((server, port))



data = sock.recv(1024)
print data

data = sock.recv(30)
print data          

for x in range(10000):
    if data == "Knock knock.\n":
        sock.send("Who's there?")
        data = sock.recv(1024)
        print data
    else:
        word = data.partition(".")[0] + " who?"     
        print word                                  
        sock.send(word)
        data = sock.recv(5000)
        print data







    

