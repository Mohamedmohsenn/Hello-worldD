import random
a=0
x=["A","B","C","D","E","F","G","H","I","J","A","B","C","D","E","F","G","H","I","J"]
random.shuffle(x)
y=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
m=[]
l=[]
sum1=0
sum2=0
while True :
        try :
            print("welcome : " + str(y))
            while True :
                y6=list(input("Player#1-score " + str(sum1) + ":" ).split(" "))
                if len(y6) == 2 :
                        z1=int(y6[0])
                        z2=int(y6[1])
                        if (z1!=0) and (z2!=0) :
                            y1=z1-1
                            y2=z2-1
                            if (z1 not in m) and (z2 not in m) and (z1 not in l) and (z2 not in l) :
                                if x[y1]==x[y2] :
                                    m.append(z1)
                                    m.append(z2)
                                    y[y1]=x[y1]
                                    y[y2]=x[y2]
                                    print("welcome : " + str(y))
                                    y[y1]="*"
                                    y[y2]="*"
                                    print("screen is cleared\n")
                                    sum1=sum1+1
                                    if y==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] and sum1>sum2 :
                                        print("player 1 is the winner")
                                        a=1
                                        break
                                    elif y==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] and sum2>sum1 :
                                        print("player 2 is the winner")
                                        a=1
                                        break 
                                    elif y==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] and sum2==sum1 :
                                        print("draw")
                                        a=1
                                        break 
                                else :
                                    y[y1]=x[y1]
                                    y[y2]=x[y2]
                                    print("welcome : " + str(y))
                                    print("screen is cleared\n")
                                    if (z1>9) and (z1<20) :
                                        y[y1]=z1-10
                                    elif z1==20 :
                                        y[y1]=0
                                    elif z1<=9 :
                                        y[y1]=z1   
                                    if (z2>9) and (z2<20) :
                                        y[y2]=z2-10
                                    elif z2==20 :
                                        y[y2]=0
                                    elif z2<=9 :
                                        y[y2]=z2
                                break        
                            else :
                                print("please dont choose a star number")
                        else :
                            print("please enter two integar number from 1 to 20 and thers a space between them\n")
                else:
                        print("please enter two integar number from 1 to 20 and thers a space between them\n") 
            if a==1 :
                break 
            print("welcome : " + str(y))
            while True :
                y7=list(input("Player#2-score " + str(sum2) + ":"  ).split(" "))
                if len(y7) == 2 :
                        b1=int(y7[0])
                        b2=int(y7[1])
                        if (b1!=0 and b2!=0) :
                            y3=b1-1
                            y4=b2-1
                            if (b1 not in l) and (b2 not in l) and (b1 not in m) and (b2 not in m) :
                                if x[y3]==x[y4] :
                                    l.append(b1)
                                    l.append(b2)
                                    y[y3]=x[y3]
                                    y[y4]=x[y4]
                                    print("welcome : " + str(y))
                                    print("screen is cleared\n")
                                    y[y3]="*"
                                    y[y4]="*"
                                    sum2=sum2+1
                                    if y==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] and sum1>sum2 :
                                        print("player 1 is the winner")
                                        a=1
                                        break 
                                    elif y==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] and sum2>sum1 :
                                        print("player 2 is the winner")
                                        a=1
                                        break
                                    elif y==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] and sum2==sum1 :
                                        print("draw")
                                        a=1
                                        break 
                                else :
                                    y[y3]=x[y3]
                                    y[y4]=x[y4]
                                    print("welcome : " + str(y))
                                    print("screen is cleared\n")
                                    if (b1>9) and (b1<20) :
                                        y[y3]=b1-10
                                    elif b1==20 :
                                        y[y3]=0
                                    elif b1<=9 :
                                        y[y3]=b1    
                                    if b2>9 and b2<20 :
                                        y[y4]=b2-10
                                    elif b2==20 :
                                        y[y4]=0
                                    elif b2<=9 :
                                        y[y4]=b2
                                break
                            else :
                                print("please dont enter a star number")
                        else :
                            print("please enter two integar number from 1 to 20 and thers a space between them\n")
                else :
                        print("please enter two integar number from 1 to 20 and thers a space between them\n")
            if a==1 :
                break
        except :
            print("please enter two integar number from 1 to 20 and thers a space between them\n")

    
    
    
