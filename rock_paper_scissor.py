def rock_papaer_scissor_play(num1,num2,bit1,bit2):
    b1 = int(num1[bit1]) % 3
    b2 = int(num2[bit2]) % 3
    if(player1[b1]==player2[b2]):
        print("Draw")
    elif(player1[b1]=='Rock' and player2[b2]=='Paper'):
        print("Player 2 Wins!!")
    elif(player1[b1]=='Rock' and player2[b2]=='Scissor'):
        print("Player1 Wins!!")
    elif (player1[b1] == 'Scissor' and player2[b2] == 'Paper'):
        print("Player1 Wins!!")
    elif (player1[b1] == 'Scissor' and player2[b2] == 'Rock'):
        print("Player2 Wins!!")
    elif (player1[b1] == 'Paper' and player2[b2] == 'Scissor'):
        print("Player2 Wins!!")
    elif (player1[b1] == 'Paper' and player2[b2] == 'Rock'):
        print("Player1 Wins!!")


player1={0:"Rock",1:"Paper",2:"Scissor"}
player2={0:"Rock",1:"Scissor",2:"Paper"}

while(1):
    num1 = input("Player1! , Enter your 5 digit number")
    num2 = input("Player2! , Enter your 5 digit number")
    bit1 = int(input("Player1!, Enter your secret bit position"))
    bit2 = int(input("Player2!, Enter your secret bit position"))
    rock_papaer_scissor_play(num1,num2,bit1,bit2)
    ch = input("Do you want to continue? y/n")
    if(ch=='n'):
        break
