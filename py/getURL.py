import re
f = open('../src/script.js')
re = re.compile('http://.+')
for line in f:
    m = re.search(line)
    if m:
        print "\"" + m.group(0) + "\","