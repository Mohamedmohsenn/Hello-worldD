list=[1,2,3,4,5,6,7,8,9]
m=[]
j=[]
sum1=0
sum2=0
print("Note for the two players : please pick a number from 1 to 9 and please the number which was choosen before dont choose it again")
while True :
        while True :
                print("\n")
                print("Please player 1 choose a number from this list : " + str(list))
                player_1=float(input("its player 1 tern : " ))
                m.append(player_1)
                if player_1 in list :
                        break
                else :
                        print("the choosen number has been choosen before or the number you choose is out of range please player 1 choose a number again")
        list.remove(player_1)
        if len(m)<=3 :
                sum1=sum1+player_1
        if sum1==15 and len(m)>2 :
                print("Player 1 is the winner")
                break
        elif len(m)==4 :
                sum1=m[0]+m[1]+m[2]
                if sum1==15 :
                        print("player 1 is the winner")
                        break
                sum1=m[0]+m[1]+m[3]
                if sum1==15 :
                        print("player 1 is the winner")
                        break
                sum1=m[0]+m[2]+m[3]
                if sum1==15 :
                        print("player 1 is the winner")
                        break
                sum1=m[1]+m[2]+m[3]
                if sum1==15 :
                        print("player 1 is the winner")
                        break
        elif len(m)==5 :
                sum1=m[0]+m[1]+m[4]
                if sum1==15 :
                        print("player 1 is the winner")
                        break
                sum1=m[0]+m[2]+m[4]
                if sum1==15 :
                        print("player 1 is the winner")
                        break
                sum1=m[0]+m[3]+m[4]
                if sum1==15 :
                        print("player 1 is the winner")
                        break
                sum1=m[1]+m[2]+m[4]
                if sum1==15 :
                        print("player 1 is the winner")
                        break
                sum1=m[1]+m[3]+m[4]
                if sum1==15 :
                        print("player 1 is the winner")
                        break
                sum=m[2]+m[3]+m[4]
                if sum1==15 :
                        print("player 1 is the winner")
                        break
        if sum1!=15 and sum2!=15 and len(list)==0 :
                print("Draw")
                break
        while True :
                print("\n")
                print("Please player 2 choose a number from this list : " + str(list))
                player_2=float(input("Its player 2 tern : " ))
                j.append(player_2)
                if player_2 in list :
                        break
                else :
                        print("The choosen number has been choosen before or the number you choose is out of the range please player 2 enter a number again")
        list.remove(player_2)
        if len(j)<=3 :
                sum2=sum2+player_2
        if sum2==15 and len(j)>2 :
                print("player 2 is the winner")
                break
        elif len(j)==4 :
                sum2=j[0]+j[1]+j[2]
                if sum2==15 :
                        print("player 2 is the winner")
                        break
                sum2=j[0]+j[1]+j[3]
                if sum2==15 :
                        print("player 2 is the winner")
                        break
                sum2=j[0]+j[2]+j[3]
                if sum2==15 :
                        print("player 2 is the winner")
                        break
                sum2=j[1]+j[2]+j[3]
                if sum2==15 :
                        print("player 2 is the winner")
                        break

        

    
        
        
    
    
    
    
        
