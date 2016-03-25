
import sys, os, sqlite3
in_file = os.path.expanduser('History')
out_file = os.path.expanduser('output.txt')

html_escape_table = {
	"&": "&amp;",
	'"': "&quot;",
	"'": "&#39;",
	">": "&gt;",
	"<": "&lt;",
	}
def html_escape(text):
	return ''.join(html_escape_table.get(c,c) for c in text)
def sanitize(string):
	res = ''
	string = html_escape(string)

	for i in range(len(string)):
		if ord(string[i]) > 127:
			res += '&#x%x;' % ord(string[i])
		else:
			res += string[i]

	return res
connection = sqlite3.connect(str(in_file))
curs = connection.cursor()
out = open(out_file, 'w')



curs.execute("SELECT url, title FROM urls")

for row in curs:
	if len(row[1]) > 0:
		out.write('"%s" \n' % (sanitize(row[0])))

connection.close()
out.close()

#row[1] will give you title of the page
