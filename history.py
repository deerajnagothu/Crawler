
import sys, os, sqlite3


# html escaping code from http://wiki.python.org/moin/EscapingHtml

in_file = os.path.expanduser(sys.argv[1])
out_file = os.path.expanduser(sys.argv[2])

connection = sqlite3.connect(in_file)
curs = connection.cursor()
#out = open(out_file, 'w')
out1=open(out_file, 'w')

#out.write("""<!DOCTYPE NETSCAPE-Bookmark-file-1>

#<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
#<title>Bookmarks</title>
#<h1>Bookmarks</h1>

#<dl><p>

#<dl><dt><h3>History</h3>

#<dl><p>""")
out1.write("History")
curs.execute("SELECT url, title FROM urls")
for row in curs:
        print(str(row[1]))
"""
for row in curs:
        if len(row[1]) > 0:
                print(row[0],row[1])
                out1.write(sanitize(row[0]), sanitize(row[1]))
"""		
connection.close()

out1.write("End")

out1.close()
#out.write('<dt><a href="%s">%s</a>\n' % (sanitize(row[0]), sanitize(row[1])))
