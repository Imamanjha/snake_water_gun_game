#snake water gun game
#write a python program in which you enter s w or g then as you enter computer should declare you as a winner or loser
#now you have to play this game for 10 times and after that one who wins the most would be declared as winner also how
#many times who won
import random
list=["snake","water","gun"]
print("There would be 10 games between you and the computer and one who wins most of them would be termed as winner")
d=0
w=0
l=0
def draw():
    global d
    d=d+1
    return d
def won():
    global w
    w=w+1
    return w
def lost():
    global l
    l=l+1
    return l
i=1
while i<11:
    a = random.choice(list)
    print("Game no.",i)
    print("What do you want to choose \n1 for snake \n2 for water \n3 for gun")
    b = int(input())#b is human response
    if a == "snake" :
        if b==1:
            print("The game is a draw")
            draw()
        elif b==2:
            print("Sorry!! You lost")
            lost()
        elif b==3:
            print("Woohooo! You Won!!")
            won()
    if a == "water" :
        if b == 1:
            print("Woohooo! You Won!!")
            won()
        if b == 2:
            print("The game is a draw")
            draw()
        if b == 3:
            print("Sorry!! You lost")
            lost()
    if a == "gun":
        if b == 1 :
            print("Sorry!! You lost")
            lost()
        if b == 2 :
            print("Woohooo! You Won!!")
            won()
        if b == 3 :
            print("The game is a draw")
            draw()
    i=i+1
print("games won by computer- ",l)
print("games won by you- ",w)
print("games tied between you and computer- ",d)
print("FINAL RESULT:")
if w>l:
    print("Hurray!!you won")
elif w==l :
    print("The game is tied")
else:
    print("Computer won")



