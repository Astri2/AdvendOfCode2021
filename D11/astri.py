from copy import deepcopy

def flash(matrice,x,y) -> int: #returns nb of new flashes
    if matrice[x][y][0] >= 10:
        matrice[x][y] = [0,True]
        xmax = len(matrice)-1
        ymax = len(matrice[x])-1
        flashes=0
        for j in range(-1+(x==0),2-(x==xmax),1):
            for k in range(-1+(y==0),2-(y==ymax),1):
                if(j!=0 or k!=0):
                    if(matrice[x+j][y+k][1] == False):
                        matrice[x+j][y+k][0]+=1
                        flashes+=flash(matrice,x+j,y+k)
        return 1+flashes
    else: return 0

def printmatrice(matrice):
    disp=[]
    for line in matrice:
        disp.append("")
        for value in line:
            disp[-1]+=str(value[0]) + " " + (" " if value[0] < 10 else "")
    return disp

def day11(lines):
    matrice = deepcopy(lines)
    nb_fish = len(matrice)*len(matrice[0])
    flashes=0
    for i in range(400):
        old_flashes=flashes
        matrice = [[[k[0]+1,False] for k in line] for line in matrice] #gain +1 energy for each
        for x in range(len(matrice)):
            for y in range(len(matrice[x])):
                    flashes+=flash(matrice,x,y)

        if(old_flashes+nb_fish==flashes): #part2, flash simultaneously
            print("day",str(i+1))
            break

    print(flashes)

if __name__ == "__main__":
    f = open("AdventOfCode2021\\D11\\input.txt")
    matrice = [[[int(k),False] for k in line] for line in f.read().splitlines()]
    day11(matrice)