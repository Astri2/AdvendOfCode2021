import re

def day10(lines):
    corr_score=0
    miss_scores=[]
    i=0
    chunks=[]
    while i < len(lines):
        line = lines[i]
        for c in line:
            if re.match(r"(\(|\[|\{|\<)",c):
                chunks.append(c)
            else:
                if re.match(r"(\(\)|\[\]|\{\}|\<\>)",chunks[-1]+c):
                    chunks.pop()
                else:
                    print(chunks[-1], "and",c,"are not compatible")
                    corr_score += (3 if c == ")" else 57 if c == "]" 
                        else 1197 if c == "}" else 25137)
                    lines.remove(line)
                    chunks=[]
                    i-=1
                    break
        score=0
        while(len(chunks)!=0):
            score=score*5 + (1 if chunks[-1] == "(" else 2 if chunks[-1] == "["
                else 3 if chunks[-1] == "{" else 4)
            chunks.pop()
        if score!=0:miss_scores.append(score)
        i+=1
    print(corr_score)
    miss_scores.sort()
    print(miss_scores[(len(miss_scores)-1)//2])
    
if __name__=="__main__":
    f = open("AdventOfCode2021\\D10\\input.txt")
    lines = f.read().splitlines()
    day10(lines)