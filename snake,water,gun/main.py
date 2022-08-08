#snake, water and gun game
print("5 rounds")
import random
you=0
computer=0
draw=0
for i in range (1,6,1):
    print("round ",i)
    opt=["snake", "water", "gun"]
    game=random.choice(opt)
    x=input("choose between snake,water or gun: ")

    print("computer:", game) #computer
    p="computer wins"
    q="you wins"
    r="match draw"
    if (game=="snake" and x=="water"):
        print(p)
        computer+=1
    elif (game=="gun" and x=="water"):
        print(q)
        you+=1
    elif (game=="water" and x=="gun"):
        print(p)
        computer+=1
    elif (game=="snake" and x=="gun"):
        print(q)
        you+=1
    elif (game=="gun" and x=="snake"):
        print(p)
        computer+=1
    elif (game=="water" and x=="snake"):
        print(q)
        you+=1
    else:
        print(r)
        draw+=1
print(f"\nyour score: {you} \ncomputer score: {computer} \ndraw match: {draw}")
if (you<computer):
    print("computer is winner")
elif (you>computer):
    print("you are winner")
else:
    print("play again")