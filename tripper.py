#!/usr/bin/python
import sys, re, string, crypt

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

x = 0
y = 0

if len(sys.argv) != 2:
    print "Tripper requires exactly one argument string that should be in the tripcode."
    sys.exit()

#mackie done: 34732252
#4chan 38759849 48531118
#ethoxy 6885633
#sakaki 155400000
while True:
    if re.search(sys.argv[1],string.lower(mktripcode(str(x))))>-1:
        print x
        print '########### TRIPCODE ###########\n'+mktripcode(str(x))+'\n########### TRIPCODE ###########\n'
    elif x==y:
        print x
        y=y+100000
    x=x+1
