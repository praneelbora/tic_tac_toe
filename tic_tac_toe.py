import pygame


list=[['_','_','_'],['_','_','_'],[' ',' ',' ']]
def check():
    for i in range(3):
        if  (list[i][0]==list[i][1]==list[i][2] and list[i][0]!=' ' and list[i][0]!='_'):   #rows
            return list[i][0]
        elif(list[0][i]==list[1][i]==list[2][i] and list[0][i]!=' ' and list[0][i]!='_'):   #columns
            return list[0][i]

    if(list[0][0]==list[1][1]==list[2][2] and list[1][1]!=' ' and list[1][1]!='_'):  #diagonal 1
        return list[1][1]
    if(list[0][2]==list[1][1]==list[2][0] and list[1][1]!=' ' and list[1][1]!='_'):  #diagonal 2
        return list[1][1]
    return -1
def printf():
    print()
    for i in {0,1,2}:
        for j in {0,1,2}:
            print(list[i][j],end='')
            if(j<2):
                print("|",end='')
        print()
    print()   
def cond(inp):
    if(inp>=10):
        return 1
    if list[(int)((inp-1)/3)][(inp-1)%3]=='X' or list[(int)((inp-1)/3)][(inp-1)%3]=='O':
        return 1
    return 0
            
check()     
turn=1
clock = pygame.time.Clock()

print("\nThese are the numberings on the grid:")
print("1|2|3\n4|5|6\n7|8|9")
for i in range(10):
    clock.tick(1)
while(True):
    printf()
    inp=''
    if (turn%2==1):
        print("X plays\nWhich block do you choose? ")
        inp=int(input())
        if(cond(inp)==1):
            print("\nWrong input, please play again")
            continue
    if (turn%2==0):
        print("O plays\nWhich block do you choose? ")
        inp=int(input())
        if(cond(inp)==1):
            print("\nWrong input, please play again")
            continue
    list[(int)((inp-1)/3)][(inp-1)%3]='X' if turn%2==1 else 'O'
    if(check()!=-1):
        printf()
        print(check()," Wins\n")
        break
    turn+=1
    if turn==10:
        printf()
        print("\nDraw\n")
        break