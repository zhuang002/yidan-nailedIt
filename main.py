class Boundle:
    height: int
    count: int


boundleMap: dict[int, int] = {}
heights: list[int] = []

def readIn():
    input()
    boards = input().split(' ')
    for board in boards:
        h = int(board)
        if h in boundleMap:
            boundleMap[h] = boundleMap[h]+1
        else:
            boundleMap[h] = 1
            heights.append(h)


readIn()
heights.sort()

minHeight = heights[0]*2
maxHeight = heights[-1]*2

maxLength = 0
for height in range(minHeight, maxHeight+1):
    length = 0
    for shorter in heights:
        longer = height - shorter
        if longer == shorter:
            length += boundleMap[shorter]/2
        elif longer > shorter:
            count1 = boundleMap[shorter]
            count2 = boundleMap[longer]
            if count1 > count2:
                length += count2
            else:
                length += count1
        else:
            break
    if maxLength < length:
        maxLength = length

print(maxLength)


