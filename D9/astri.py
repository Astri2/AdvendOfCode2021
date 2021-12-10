def part1(matrice):
    danger = 0
    xmax = len(matrice)-1
    for x in range(len(matrice)):
        ymax = len(matrice[x])-1
        for y in range(len(matrice[x])):
            if(
              (x==0 or matrice[x][y] < matrice[x-1][y]) and
              (x==xmax or matrice[x][y] < matrice[x+1][y]) and
              (y==0 or matrice[x][y] < matrice[x][y-1]) and
              (y==ymax or matrice[x][y] < matrice[x][y+1])
            ):
                danger+=matrice[x][y]+1
    return danger

from copy import deepcopy
def get_bassin_size(matrice,x,y):
    xmax = len(matrice)-1
    ymax = len(matrice[x])-1

    if matrice[x][y] == 9:
        return 0
    matrice[x][y]=9
    return (
        1 + 
        get_bassin_size(matrice,x+1-(x==xmax),y) +
        get_bassin_size(matrice,x-1+(x==0),y) +
        get_bassin_size(matrice,x,y+1-(y==ymax)) +
        get_bassin_size(matrice,x,y-1+(y==0))
    )

def part2(matrice):
    matrice = deepcopy(matrice)
    bassins=[]
    for x in range(len(matrice)):
        for y in range(len(matrice[x])):
            if(matrice[x][y] != 9):
                bassins.append(get_bassin_size(matrice,x,y))
    bassins.sort()
    return bassins[-1]*bassins[-2]*bassins[-3]

if __name__=="__main__":
    f = open("AdventOfCode2021\\D9\\input.txt")
    matrice = [[int(k) for k in line] for line in f.read().splitlines()]

    print(part2(matrice))