print(min([[sum([abs(crab-i)*(abs(crab-i)+1)/2 for crab in tab]) for i in range(max(tab))] for tab in [[int(k) for k in open("AdventOfCode2021\\D7\\input.txt",'r').read().split(",")]]][0]))