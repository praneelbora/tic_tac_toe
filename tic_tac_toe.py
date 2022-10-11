list=[['1','2','3'],['4','5','6'],['7','8','9']]
win='a'
c1=0
c2=0
c3=0
d1=0
d2=0
def check():
    win=' '
    cnt=0
    for i in {0,1,2}:
        if(list[i][0]==list[i][1]and list[i][1]==list[i][2] and list[i][0]!=' '):
            return list[i][0]
        elif(list[0][i]==list[1][i] and list[1][i]==list[2][i]and list[0][i]!=' '):
            return list[0][i]
    if(list[0][0]==list[1][1]and list[1][1]==list[2][2] and list[1][1]!=' '):
        return list[0][0]
    if(list[0][2]==list[1][1]and list[1][1]==list[2][0] and list[1][1]!=' '):
        return list[0][0]
    return -1
check()
def printf():
    print("\n")
    for i in {0,1,2}:
        for j in {0,1,2}:
            print(list[i][j],end='')
            if(j<2):
                print("|",end='')
        print()
    print("\n")
            
turn=0
while(True):
    printf()
    if (turn%2==0):
        print("X plays\nWhich block do you choose? ")
        inp=int(input())
        
    if (turn%2==1):
        print("O plays\nWhich block do you choose? ")
        inp=int(input())
    turn+=1
    break