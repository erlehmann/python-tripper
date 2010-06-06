#!/usr/bin/python
import sys, re, string, crypt

# Import Psyco if available
try:
    import psyco
    psyco.full()
    print "using Psyco"
except ImportError:
    pass

def mktripcode(pw):
    pw = pw.decode('utf_8', 'ignore') \
        .encode('shift_jis', 'ignore')    \
        .replace('"', '&quot;')      \
        .replace("'", '')           \
        .replace('<', '&lt;')        \
        .replace('>', '&gt;')        \
        .replace(',', ',')
    salt = (pw + '...')[1:3]
    salt = re.compile('[^\.-z]').sub('.', salt)
    salt = salt.translate(string.maketrans(':;<=>?@[\\]^_`', 'ABCDEFGabcdef'))
    trip = crypt.crypt(pw, salt)[-10:]
    return trip

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print "Tripper requires one or two arguments. First argument is the string that should be in the tripcode, second is the start value for brute-forcing."
    sys.exit()

try:
    x = int(sys.argv[2])
except IndexError:
    x = 0

#mackie done: 34732252
#4chan 38759849 48531118
#ethoxy 6885633
#sakaki 155400000
while True:
    if re.search(sys.argv[1],string.lower(mktripcode(str(x))))>-1:
        print x, ":", mktripcode(str(x))
    elif x % 100000 == 0:
        print x
    x += 1
