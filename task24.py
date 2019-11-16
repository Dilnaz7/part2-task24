print ("1 - dlya Far-Cel 2 - Cel v Far")
vybor=int(input())
if vybor == 1:
    print ("Вводите число Far ")
    Far = int(input())
    Cel = (Far-32)*5/9
    print (Cel)
else: 
    cel = int(input("VVedite Celsius"))
    far = cel*9/5 +32
    print (far)
    