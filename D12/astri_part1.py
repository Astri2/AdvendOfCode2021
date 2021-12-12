def get_path(map,pos,current):
    paths_from_here=[]
    for next in map[pos]:
        if(next in current and not next.isupper()):
            paths_from_here.append(list(current))
        else:
            if next == "end":
                paths_from_here.append(list(current)+[next])
            else:
                paths_from_here.extend(get_path(map,next,current+[next]))
    return paths_from_here

def print_paths(paths):
    for path in paths:
        print(path)

def part1(map):
    paths = [path for path in get_path(map,"start",["start"]) if path[-1]=="end"]
    print(len(paths))


def get_caves_connections(input)->dict:
    dic={}
    for line in input:
        if(line[0] in dic.keys()):
            dic[line[0]].append(line[1])
        else : dic[line[0]] = [line[1]]
        if(line[1] in dic.keys()):
            dic[line[1]].append(line[0])
        else : dic[line[1]] = [line[0]]
    return(dic)


if __name__=="__main__":
    f = open("AdventOfCode2021\\D12\\input.txt","r")
    input = [line.split("-") for line in f.read().splitlines()]
    part1(get_caves_connections(input))

#40mins