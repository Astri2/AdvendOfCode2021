def ex1(values):
    counter = 0
    for i in range(1,len(values)):
        if values[i-1] < values[i]:
            counter+=1
    return counter

def ex2(values):
    sums = []
    for i in range(0,len(values)-2):
        sums.append(values[i]+values[i+1]+values[i+2])
    return ex1(sums)
    

def main():
    Lines = [int(k) for k in open('ex1_list.txt','r').readlines()]
    print(ex1(Lines))
    print(ex2(Lines))

if(__name__ == '__main__'):
    main()

