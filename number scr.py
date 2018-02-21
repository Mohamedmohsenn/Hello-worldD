list=[1,2,3,4,5,6,7,8,9]
a=0
m=[]
j=[]
print("for the two players pick a number from 1 to 9 and please the number which was choosen before dont choose it again.")
while True :
        while True :
                try :
                        while True :
                                print("\n-------\nPlease player 1 choose a number from this list : " + str(list))
                                player_1=int(input("\nIts player 1 tern : " ))
                                if (player_1 not in m) and (player_1 not in j) and (player_1<10) and (player_1>0) :
                                        m.append(player_1)
                                if player_1 in list :
                                        break
                                else :
                                        print("the choosen number has been choosen before or the number you choose is out of range please player 1 choose a number again")
                        list.remove(player_1)
                        if len(m)==3 :
                                if m[0]+m[1]+m[2]==15 :
                                        print("Player 1 is the winner")
                                        a=1
                                        break
                        elif len(m)==4 :
                                if m[0]+m[1]+m[3]==15 or m[0]+m[2]+m[3]==15 or m[1]+m[2]+m[3]==15 :
                                        print("player 1 is the winner")
                                        a=1
                                        break
                        elif len(m)==5 :
                                if m[0]+m[1]+m[4]==15 or m[0]+m[2]+m[4]==15 or m[0]+m[3]+m[4]==15 or m[1]+m[2]+m[4]==15 or m[1]+m[3]+m[4]==15 or m[2]+m[3]+m[4]==15 :
                                        print("player 1 is the winner")
                                        a=1
                                        break
                                elif (m[0]+m[1]+m[4]!=15 and m[0]+m[2]+m[4]!=15 and m[0]+m[3]+m[4]!=15 and m[1]+m[2]+m[4]!=15 and m[1]+m[3]+m[4]!=15 and m[2]+m[3]+m[4]!=15)  and (len(list)==0) :
                                        print("Draw")
                                        a=1
                                        break
                        break
                except :
                        print("please just enter an INTEGAR NUMBER from the list!!!!")
        if a==1 :
                break 
        while True :
                try :
                        while True :
                                print("\n-------\nPlease player 2 choose a number from this list : " + str(list))
                                player_2=int(input("\nIts player 2 tern : " ))
                                if (player_2 not in m) and (player_2 not in j) and (player_2<10) and (player_2>0) :
                                        j.append(player_2)
                                if player_2 in list :
                                        break
                                else :
                                        print("The choosen number has been choosen before or the number you choose is out of the range please player 2 enter a number again")
                        list.remove(player_2)
                        if len(j)==3 :
                                if j[0]+j[1]+j[2]==15 :
                                        print("player 2 is the winner")
                                        a=1
                                        break
                        elif len(j)==4 :
                                if j[0]+j[1]+j[3]==15 or j[0]+j[2]+j[3]==15 or j[1]+j[2]+j[3]==15 :
                                        print("player 2 is the winner")
                                        a=1
                                        break
                        break
                except :
                        print("please just enter an INTEGAR NUMBER from the list!!!!")
        if a==1 :
                break

                        

        

    
        
        
