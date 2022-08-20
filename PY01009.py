n = input() 
hoa = 0
thuong = 0
for i in range(len(n)):
    if(n[i].isupper()):
        hoa+=1
    else:
        thuong+=1
if(hoa > thuong):
    print(n.upper())
else:
    print(n.lower())
