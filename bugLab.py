# Sara Liu, 9/28/18

import sys
import time


def neighbors(chrIndex):
    neighList = []
    global spokes
    if chr(chrIndex).isupper():
        neighList.append(chr(chrIndex).lower())
        if (chrIndex + 1) - 65 == spokes:
            neighList.append(chr(65))
        else:
            neighList.append(chr(chrIndex + 1))
    else:
        neighList.append(chr(chrIndex).upper())
        if (chrIndex - 1) == 96:
            neighList.append(chr(96 + spokes))
        else:
            neighList.append(chr(chrIndex - 1))
    return neighList


def bfsDistribution():
    # parseMe = [chr(65)]
    # dctSeen = {parseMe[0]: [1]}  # {letter: [number of paths to reach it for a certain level(index)]}
    # global depth
    # level = 0
    # while parseMe and level + 1 <= depth + 1:
    #     letter = parseMe.pop(0)
    #     level = len(dctSeen[letter]) - 1
    #     for neighbor in neighbors(ord(letter)):
    #         if neighbor not in dctSeen:
    #             parseMe.append(neighbor)
    #             dctSeen[neighbor] = []
    #             for i in range(level + 1):
    #                 dctSeen[neighbor].append(0)
    #             dctSeen[neighbor].append(1)
    #             if dctSeen[letter][level] > 1:
    #                 dctSeen[neighbor][level + 1] = dctSeen[letter][level]
    #         else:
    #             if len(dctSeen[neighbor]) - 1 < level + 1:
    #                 for i in range(len(dctSeen[neighbor]), level + 1):
    #                     dctSeen[neighbor].append(0)
    #                 dctSeen[neighbor].append(1)
    #             else:
    #                 dctSeen[neighbor][level + 1] += 1
    # return dctSeen

    parseMe = [[chr(65), 0]]  # [[letter, level]]
    global depth
    dctSeen = {parseMe[0][0]: [1] + [0] * depth}  # {letter: [number of paths to reach it for a certain level(index)]}
    while parseMe:
        letterAndLevel = parseMe.pop(0)
        letter = letterAndLevel[0]
        level = letterAndLevel[1]
        if not level + 1 <= depth:
            continue
        for neighbor in neighbors(ord(letter)):
            if neighbor not in dctSeen:
                parseMe.append([neighbor, level + 1])
                dctSeen[neighbor] = [0] * (depth + 1)
                dctSeen[neighbor][level + 1] = 1
                if dctSeen[letter][level] > 1:
                    dctSeen[neighbor][level + 1] += dctSeen[letter][level]
            else:
                parseMe.append([neighbor, level + 1])
                dctSeen[neighbor][level + 1] += 1
    return dctSeen


spokes = 5
depth = 20
if len(sys.argv) >= 2:
    spokes = int(sys.argv[1])
    if len(sys.argv) == 3:
        depth = int(sys.argv[2])
t1 = time.time()
distribution = bfsDistribution()
t2 = time.time()
totalTime = t2 - t1
print('Ways to reach ', spokes * 2, ' spots on a double spoked wheel in ', depth, ' steps')
alphaList = []
for key in distribution:
    alphaList.append(str(key + ': ' + str(distribution[key]).strip('[]')))
alphaList.sort()
for path in alphaList:
    print(path)
print('Total time: ', totalTime)
