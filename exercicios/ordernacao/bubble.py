list = [40, 30, 20, 50, 10]
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
    
def biggestInEnd(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            swapPositions(list, i, i + 1)
    return list
            
def bubbleSort(list):
    aux = len(list)
    while aux > 1:
        biggestInEnd(list)
        aux -= 1
    return list
    

print(list)
print(bubbleSort(list[:]))
print(list)