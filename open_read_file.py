fname=input("enter the text")
if len(fname)<1: fname="clown.txt"
hand = open(fname)
di=dict()
for lin in hand:
    lin =lin.strip()
    print(lin)
    wds =lin.split()
    #print(wds)
    for w in wds:
        #first solution
        # print(w,dir.get(w,-99))

        #this second solution
        oldcount=di.get(w,0)
        print(w,oldcount)
        newcount=oldcount+1
        di[w]=newcount
print(di)


        