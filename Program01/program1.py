a = 100000000
j=9
for i in range(j):
    if(i==1 | i<2):
        b=a*0
        print ("Laba bulan ke ",i," : ", b)

    if(i==2):
        c=a*0
        print ("Laba bulan ke ",i," : ", c)

    if(i>=3 and i<=4):
        d=a*0.1
        print ("Laba bulan ke ",i," : ", d)
    if(i>=5 and i<=7):
        e=a*0.5
        print ("Laba bulan ke ",i," : ", e)
    if(i==8):
        f=a*0.2
        print ("Laba bulan ke ",i," : ", f)
g =f+d+d+e+e+e+b+c
print ("Total Laba adalah", g)
        
    
    
    
