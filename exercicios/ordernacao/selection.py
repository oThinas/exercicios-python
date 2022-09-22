import list
list = list.Constants().LIST

def selectionSort(list):
  for i in range(len(list)):
    minIndex = i
    for j in range(i + 1, len(list)):
      if list[j] < list[minIndex]: # Asc: < | Desc: >
        minIndex = j
    list[i], list[minIndex] = list[minIndex],list[i]
  return list
  
print(list)
print(selectionSort(list[:]))
print(list)