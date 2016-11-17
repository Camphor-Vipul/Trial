import random

print("................Welcome to Roll the Die game................\nSo the game goes like this:\nYou have to first choose how many faced-die you would like to play with!\nThen just follow the instructions and enjoy!\n")
n_faces=int(input("Enter the number of faces you would like the die to have\n"))
while n_faces==1:
    print("That's kind of cunning! Are you afraid of facing challenges ?\nLet's try once again...\nIf you want to quit now enter 'I Quit' and if you don't enter 'I Can' without single quotes")
    result=input()
    if(result=='I Quit'):
        exit()
    elif(result=='I Can'):
        n_faces=int(input("Enter the number of faces you would like the die to have\n"))
ans='Y'
while ans=='Y':
    a=int(input("Guess number that the die would show up !\n"))
    if a<1 and a>n_faces:
        print("Enter valid number\n")
    else:
         b=random.randrange(1,n_faces+1)
         if(a==b):
             print("You have got some real guts you guessed it right!!\n")
         else:
             print("You were close, better luck next time\n")
    ans=input("Wanna give another shot(Y/N)?\n")
