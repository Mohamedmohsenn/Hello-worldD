y=21
x=1
a=0
a=[1,2,3]
while True :
    try :
        l=" ".join(map(str,a))
        print("There’s "+str(y)+" coins")
        players=int(input("please player "+ str(x) +" choose from "+l+" coins  : "))
        print("\n")
        if players==1 :
            y=y-1
            if y>0 :
                if y==1 :
                    print("player "+str(x)+" is the winner")
                    a=1
                    break
                elif y>1 and y<4 :
                    if y==3 :
                        a.remove(3)
                    elif y==2 :
                        a.remove(2)
                if x==1 :
                    x=2
                else :
                    x=1
            elif y<=0 :
                y=y+1
        elif players==2 :
            y=y-2
            if y>0 :
                if y==1 :
                    print("player "+str(x)+" is the winner")
                    a=1
                    break
                elif y>1 and y<4 :
                    if y==3 :
                        a.remove(3)
                    elif y==2 :
                        a.remove(2)
                        a.remove(3)
                if x==1 :
                    x=2
                else :
                    x=1
            elif y<=0 :
                y=y+2
        elif players==3 :
            y=y-3
            if y>0 :
                if y==1 :
                    print("player " +str(x)+" is the winner")
                    a=1
                    break
                elif y>1 and y<4 :
                    if y==3 :
                        a.remove(3)
                    elif y==2 :
                        a.remove(2)
                        a.remove(3)
                if x==1 :
                    x=2
                else :
                    x=1
            elif y<=0 :
                y=y+3
    except :
        print("\n")
        
    
    
