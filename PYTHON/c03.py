
"""
Fails:c02.py
Autors:Mārtiņš Cakeus
Datums:21.12.2017
Tiek nolasiits fails c01.txt
1.Katrs baits tiek interpretets ka skaitlis
un izdrukats sedecimaalaa formata.
2.Katrs baits, kas interpreteets kaa skaitlis
tiek izdrukaats kaasimbols.
Failu aizver.
"""
f = open("meta.bin" ,"rb")                        #atvera, failu lasiishanai
f.seek(0)                                           #failu attin uz asskumu

while 1:
    b = f.read(1)                                   #nolasa vienu baitu
    if not b:                                #ja baits nav nolasams -- nav ko lasit
        break                                 #paartraucam lasiishanu
    #print hex(ord(b))                               #baitu drukaa ka sedecimaalu skaitli
    print chr(ord(b))                               #baitu drukaa ka simbolu
                                           #metode ord() simbolu stgriez ka skaitli
                                           #failu ciet!




d = open("data.bin" ,"rb")                        #atvera, failu lasiishanai
d.seek(1)                                           #failu attin uz asskumu

while 1:
    a = d.read(1)                                   #nolasa vienu baitu
    if not a:                                #ja baits nav nolasams -- nav ko lasit
        break                                 #paartraucam lasiishanu
    #print hex(ord(a))                               #baitu drukaa ka sedecimaalu skaitli
    print chr(ord(a))                             #baitu drukaa ka simbolu
                                        #metode ord() simbolu stgriez ka skaitli
f.close()
d.close

