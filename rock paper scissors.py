import random,sys

print('ROCK,PAPER,SCISSORS')

wins=0
loss=0
ties=0

while True:
    print('%s wins,%s loss,%s ties ' %(wins,loss,ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        a=input()
        if a=='q':
            sys.exit()
        if a=='r' or a=='p' or a=='s':
            break
        print('Type one of r,p,s or q')

    if a=='r':
        print('ROCK versus')
    elif a=='p':
        print('PAPER versus')
    elif a=='s':
        print('SCISSORS versus')

    x=random.randint(1,3)
    if x==1:
        c='r'
        print('ROCK')
    elif x==2:
        c='p'
        print('PAPER')
    elif x==3:
        c='s'
        print('SCISSORS')


    if a ==c:
        print('It is a tie')
        ties=ties+1
    elif a=='r' and c=='s':
        print('It is a win')
        wins=wins+1
    elif a=='p' and c=='r':
        print('It is a win')
        wins=wins+1
    elif a=='s' and c=='p':
        print('It is a win')
        wins=wins+1
    elif a=='r' and c=='p':
        print('It is a loss')
        loss=loss+1
    elif a=='p' and c=='s':
        print('It is a loss')
        loss=loss+1
    elif a=='s' and c=='r':
        print('It is a loss')
        loss=loss+1

