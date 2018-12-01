#!/usr/bin/python3
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()
year = form.getvalue("Year")
datetype = form.getvalue("date")
''''ef normalise(text):
	#fuction to normaile text
	text = text.strip(" ")
	if text > 4:
		print("year out of range")
	else: 
		for i in list(text):
			if i not in range(0,9):
				print("%s is not numeric year" % text)
			else: '''

print('Content-Type: text/html; charset=utf-8')
print('')

print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<title>Result</title>')
print('</head>')
print('<body>')
print('<header')
print('</header')
print("<nav>")
print('</nav>')
print('<section>')
print('<h1>Hello world</h1')
print('<p>%s</p>' % (year))
print('<p>%s</p>'%(datetype))
print('</section')
print('</body')
print('</html>')
