
f = open("meta.bin","rb")

f.seek(0)
f.seek(1)
while 1:
    b = f.read(1)
    if not b:
        break
    print hex(ord(b))
    print chr(ord(b))

f1 = open("data.bin","rb")
f1.seek(1)
while 1:
    a = f1.read(1)
    if not a:
        break
    print hex(ord(a))
    print chr(ord(a))
    hex(ord(a) ^ ord(b))
    chr(ord(a) ^ ord(b))


f.close()



