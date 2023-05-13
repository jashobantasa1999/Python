
def repfind(a):
    b  = set(a)
    cout =0
    for i in b:
        for   j in a:
            if(i ==j ):
                cout = cout+1
        print (i,"is repeated ",cout ,"times");
        cout =0


a =[]
for i in range (5):
    b = int(input("enter a number"))
    a.append(b)


repfind(a)